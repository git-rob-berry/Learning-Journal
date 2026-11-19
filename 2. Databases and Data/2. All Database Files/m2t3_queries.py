import sqlite3

conn = sqlite3.connect("airport_booking.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")


# M2T3 queries go below

# ==========================================
# 1A - INNER JOIN
# WHO BOOKED WHICH FLIGHT?
# ==========================================

print("\n--- BOOKING AND FLIGHT DETAILS ---")

cursor.execute("""
SELECT
    b.booking_id,
    c.first_name || ' ' || c.last_name AS customer,
    f.flight_no,
    da.iata_code AS dep,
    aa.iata_code AS arr,
    b.status,
    b.booked_at
FROM booking b
JOIN customer c
    ON c.customer_id = b.customer_id
JOIN flight f
    ON f.flight_id = b.flight_id
JOIN airport da
    ON da.airport_id = f.dep_airport
JOIN airport aa
    ON aa.airport_id = f.arr_airport
ORDER BY b.booked_at DESC
LIMIT 20;
""")

for row in cursor.fetchall():
    print(row)

# ==========================================
# 1B - LEFT JOIN
# BOOKINGS AND THEIR PAYMENTS
# ==========================================

print("\n--- BOOKINGS AND TOTAL PAID ---")

cursor.execute("""
SELECT
    b.booking_id,
    b.status,
    c.email,
    COALESCE(SUM(p.amount), 0) AS total_paid
FROM booking b
LEFT JOIN payment p
    ON p.booking_id = b.booking_id
JOIN customer c
    ON c.customer_id = b.customer_id
GROUP BY
    b.booking_id,
    b.status,
    c.email
ORDER BY b.booked_at DESC
LIMIT 20;
""")

for row in cursor.fetchall():
    print(row)

# ==========================================
# 2A - UNPAID BOOKINGS
# LEFT JOIN METHOD
# ==========================================

print("\n--- UNPAID BOOKINGS - LEFT JOIN METHOD ---")

cursor.execute("""
SELECT
    b.booking_id,
    b.status,
    c.email,
    b.base_fare
FROM booking b
JOIN customer c
    ON c.customer_id = b.customer_id
LEFT JOIN payment p
    ON b.booking_id = p.booking_id
WHERE b.status <> 'CANCELLED'
  AND p.payment_id IS NULL
ORDER BY b.booked_at DESC
LIMIT 20;
""")

for row in cursor.fetchall():
    print(row)


# ==========================================
# 2B - UNPAID BOOKINGS
# NOT EXISTS METHOD
# ==========================================

print("\n--- UNPAID BOOKINGS - NOT EXISTS METHOD ---")

cursor.execute("""
SELECT
    b.booking_id,
    b.status,
    c.email,
    b.base_fare
FROM booking b
JOIN customer c
    ON c.customer_id = b.customer_id
WHERE b.status <> 'CANCELLED'
  AND NOT EXISTS (
      SELECT 1
      FROM payment p
      WHERE p.booking_id = b.booking_id
  )
ORDER BY b.booked_at DESC
LIMIT 20;
""")

for row in cursor.fetchall():
    print(row)

# ==========================================
# 2C - EXISTS
# CUSTOMERS WITH CONFIRMED BOOKINGS
# ==========================================

print("\n--- CUSTOMERS WITH CONFIRMED BOOKINGS ---")

cursor.execute("""
SELECT
    c.customer_id,
    c.email
FROM customer c
WHERE EXISTS (
    SELECT 1
    FROM booking b
    WHERE b.customer_id = c.customer_id
      AND b.status = 'CONFIRMED'
)
LIMIT 20;
""")

for row in cursor.fetchall():
    print(row)

# ==========================================
# 3A - SELF JOIN
# SAME-DAY OUT AND BACK FLIGHTS
# ==========================================

print("\n--- SAME-DAY OUT AND BACK FLIGHTS ---")

cursor.execute("""
SELECT
    f1.flight_no AS out_no,
    f2.flight_no AS back_no,
    da.iata_code AS dep,
    aa.iata_code AS arr,
    f1.dep_time AS dep_date
FROM flight f1
JOIN flight f2
    ON f2.dep_airport = f1.arr_airport
   AND f2.arr_airport = f1.dep_airport
   AND DATE(f2.dep_time) = DATE(f1.dep_time)
JOIN airport da
    ON da.airport_id = f1.dep_airport
JOIN airport aa
    ON aa.airport_id = f1.arr_airport
ORDER BY dep_date, dep, arr
LIMIT 20;
""")

for row in cursor.fetchall():
    print(row)

# ==========================================
# 3B - CROSS JOIN
# AIRPORT PAIRS WITH NO FLIGHT NEXT 7 DAYS
# ==========================================

print("\n--- AIRPORT PAIRS WITH NO FLIGHT NEXT 7 DAYS ---")

cursor.execute("""
SELECT
    a1.iata_code AS dep,
    a2.iata_code AS arr
FROM airport a1
CROSS JOIN airport a2
WHERE a1.airport_id <> a2.airport_id
  AND NOT EXISTS (
      SELECT 1
      FROM flight f
      WHERE f.dep_airport = a1.airport_id
        AND f.arr_airport = a2.airport_id
        AND f.dep_time BETWEEN DATETIME('now')
                           AND DATETIME('now', '+7 days')
  )
ORDER BY dep, arr
LIMIT 20;
""")

for row in cursor.fetchall():
    print(row)


# ==========================================
# 4A - BOOKINGS PER STATUS
# ==========================================

print("\n--- BOOKINGS PER STATUS ---")

cursor.execute("""
SELECT
    status,
    COUNT(*) AS bookings
FROM booking
GROUP BY status
ORDER BY bookings DESC;
""")

for row in cursor.fetchall():
    print(row)


# ==========================================
# 4B - REVENUE PER PAYMENT METHOD
# ==========================================

print("\n--- REVENUE PER PAYMENT METHOD ---")

cursor.execute("""
SELECT
    method,
    ROUND(SUM(amount), 2) AS revenue
FROM payment
GROUP BY method
ORDER BY revenue DESC;
""")

for row in cursor.fetchall():
    print(row)

# ==========================================
# 5A - BOOKINGS IN LAST 90 DAYS
# ==========================================

print("\n--- BOOKINGS BY STATUS - LAST 90 DAYS ---")

cursor.execute("""
SELECT
    status,
    COUNT(*) AS bookings
FROM booking
WHERE booked_at >= DATETIME('now', '-90 days')
GROUP BY status;
""")

for row in cursor.fetchall():
    print(row)

# ==========================================
# 5B - ROUTES WITH REVENUE OVER 1000
# LAST 30 DAYS
# ==========================================

print("\n--- HIGH REVENUE ROUTES - LAST 30 DAYS ---")

cursor.execute("""
SELECT
    da.iata_code AS dep,
    aa.iata_code AS arr,
    ROUND(SUM(p.amount), 2) AS revenue_30d
FROM payment p
JOIN booking b
    ON b.booking_id = p.booking_id
JOIN flight f
    ON f.flight_id = b.flight_id
JOIN airport da
    ON da.airport_id = f.dep_airport
JOIN airport aa
    ON aa.airport_id = f.arr_airport
WHERE p.paid_at >= DATETIME('now', '-30 days')
GROUP BY
    da.iata_code,
    aa.iata_code
HAVING SUM(p.amount) > 1000
ORDER BY revenue_30d DESC
LIMIT 20;
""")

for row in cursor.fetchall():
    print(row)

# ==========================================
# 6 - PRE-AGGREGATE PAYMENTS
# ==========================================

print("\n--- CUSTOMER BOOKINGS AND REVENUE ---")

cursor.execute("""
WITH pay AS (
    SELECT
        booking_id,
        SUM(amount) AS total_paid
    FROM payment
    GROUP BY booking_id
)

SELECT
    b.customer_id,
    COUNT(*) AS bookings,
    ROUND(
        SUM(COALESCE(pay.total_paid, 0)),
        2
    ) AS revenue
FROM booking b
LEFT JOIN pay
    ON pay.booking_id = b.booking_id
GROUP BY b.customer_id
ORDER BY revenue DESC
LIMIT 20;
""")

for row in cursor.fetchall():
    print(row)

# ==========================================
# 7A - MONTHLY BOOKINGS
# ==========================================

print("\n--- MONTHLY BOOKINGS BY STATUS ---")

cursor.execute("""
SELECT
    date(strftime('%Y-%m-01', booked_at)) AS month_start,
    COUNT(*) AS total,

    SUM(
        CASE
            WHEN status = 'CONFIRMED' THEN 1
            ELSE 0
        END
    ) AS confirmed,

    SUM(
        CASE
            WHEN status = 'PENDING' THEN 1
            ELSE 0
        END
    ) AS pending,

    SUM(
        CASE
            WHEN status = 'CANCELLED' THEN 1
            ELSE 0
        END
    ) AS cancelled

FROM booking
GROUP BY month_start
ORDER BY month_start;
""")

for row in cursor.fetchall():
    print(row)

# ==========================================
# 7B - AVERAGE FLIGHT DURATION
# ==========================================

print("\n--- AVERAGE FLIGHT DURATION BY DEPARTURE AIRPORT ---")

cursor.execute("""
SELECT
    da.iata_code AS dep,

    ROUND(
        AVG(
            (
                strftime('%s', f.arr_time)
                -
                strftime('%s', f.dep_time)
            ) / 60.0
        ),
        1
    ) AS avg_minutes

FROM flight f

JOIN airport da
    ON da.airport_id = f.dep_airport

GROUP BY da.iata_code

ORDER BY avg_minutes DESC;
""")

for row in cursor.fetchall():
    print(row)


# ==========================================
# 8A - SUBQUERY
# OUTSTANDING BOOKING VALUES
# ==========================================

print("\n--- BOOKING PAYMENT POSITION ---")

cursor.execute("""
SELECT
    b.booking_id,
    b.base_fare,

    COALESCE(
        (
            SELECT SUM(p.amount)
            FROM payment p
            WHERE p.booking_id = b.booking_id
        ),
        0
    ) AS total_paid,

    b.base_fare -
    COALESCE(
        (
            SELECT SUM(p.amount)
            FROM payment p
            WHERE p.booking_id = b.booking_id
        ),
        0
    ) AS outstanding

FROM booking b

ORDER BY b.booked_at DESC

LIMIT 20;
""")

for row in cursor.fetchall():
    print(row)

# ==========================================
# CONSOLIDATION 1
# UNPAID CONFIRMED BOOKINGS
# ==========================================

print("\n--- UNPAID CONFIRMED BOOKINGS ---")

cursor.execute("""
SELECT
    b.booking_id,
    c.email,
    b.base_fare,
    b.base_fare AS outstanding_amount

FROM booking b

JOIN customer c
    ON c.customer_id = b.customer_id

WHERE b.status = 'CONFIRMED'

AND NOT EXISTS (
    SELECT 1
    FROM payment p
    WHERE p.booking_id = b.booking_id
)

ORDER BY b.booked_at DESC;
""")

results = cursor.fetchall()

print(f"Total unpaid confirmed bookings: {len(results)}")
print("Showing first 20:")

for row in results[:20]:
    print(row)


# ==========================================
# CONSOLIDATION 2
# TOP 10 CUSTOMERS BY LIFETIME REVENUE
# ==========================================

print("\n--- TOP 10 CUSTOMERS BY LIFETIME REVENUE ---")

cursor.execute("""
WITH pay AS (

    SELECT
        booking_id,
        SUM(amount) AS total_paid

    FROM payment

    GROUP BY booking_id
)

SELECT
    c.customer_id,
    c.first_name || ' ' || c.last_name AS customer,
    c.email,

    COUNT(b.booking_id) AS booking_count,

    ROUND(
        AVG(b.base_fare),
        2
    ) AS average_fare,

    ROUND(
        SUM(COALESCE(pay.total_paid, 0)),
        2
    ) AS lifetime_revenue

FROM customer c

JOIN booking b
    ON b.customer_id = c.customer_id

LEFT JOIN pay
    ON pay.booking_id = b.booking_id

GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name,
    c.email

ORDER BY lifetime_revenue DESC

LIMIT 10;
""")

for row in cursor.fetchall():
    print(row)

# ==========================================
# CONSOLIDATION 3
# DAILY BOOKED VS PAID - LAST 14 DAYS
# ==========================================

print("\n--- DAILY BOOKED VS PAID - LAST 14 DAYS ---")

cursor.execute("""
WITH RECURSIVE dates(day) AS (

    SELECT DATE('now', '-13 days')

    UNION ALL

    SELECT DATE(day, '+1 day')
    FROM dates
    WHERE day < DATE('now')

),

booked AS (

    SELECT
        DATE(booked_at) AS day,
        COUNT(*) AS booked_count

    FROM booking

    WHERE DATE(booked_at)
          BETWEEN DATE('now', '-13 days')
              AND DATE('now')

    GROUP BY DATE(booked_at)

),

paid AS (

    SELECT
        DATE(paid_at) AS day,
        COUNT(DISTINCT booking_id) AS paid_count

    FROM payment

    WHERE DATE(paid_at)
          BETWEEN DATE('now', '-13 days')
              AND DATE('now')

    GROUP BY DATE(paid_at)

)

SELECT
    dates.day,
    COALESCE(booked.booked_count, 0) AS booked,
    COALESCE(paid.paid_count, 0) AS paid

FROM dates

LEFT JOIN booked
    ON booked.day = dates.day

LEFT JOIN paid
    ON paid.day = dates.day

ORDER BY dates.day;
""")

for row in cursor.fetchall():
    print(row)

# ==========================================
# CONSOLIDATION 4
# AIRPORT PAIRS WITH FLIGHTS BOTH WAYS
# ==========================================

print("\n--- AIRPORT PAIRS WITH FLIGHTS BOTH WAYS ---")

cursor.execute("""
WITH daily_routes AS (

    SELECT
        DATE(f.dep_time) AS flight_date,
        f.dep_airport,
        f.arr_airport,
        COUNT(*) AS flights

    FROM flight f

    GROUP BY
        DATE(f.dep_time),
        f.dep_airport,
        f.arr_airport
)

SELECT
    r1.flight_date,
    da.iata_code AS airport_1,
    aa.iata_code AS airport_2,

    r1.flights + r2.flights AS total_flights

FROM daily_routes r1

JOIN daily_routes r2
    ON r2.flight_date = r1.flight_date
   AND r2.dep_airport = r1.arr_airport
   AND r2.arr_airport = r1.dep_airport

JOIN airport da
    ON da.airport_id = r1.dep_airport

JOIN airport aa
    ON aa.airport_id = r1.arr_airport

WHERE r1.dep_airport < r1.arr_airport

ORDER BY
    total_flights DESC,
    r1.flight_date

LIMIT 20;
""")

for row in cursor.fetchall():
    print(row)


# ==========================================
# CONSOLIDATION 5
# ROUTES WITH FALLING REVENUE
# ==========================================

print("\n--- ROUTES WITH FALLING REVENUE ---")

cursor.execute("""
WITH recent_30 AS (

    SELECT
        f.dep_airport,
        f.arr_airport,
        SUM(p.amount) AS revenue_recent

    FROM payment p

    JOIN booking b
        ON b.booking_id = p.booking_id

    JOIN flight f
        ON f.flight_id = b.flight_id

    WHERE p.paid_at >= DATETIME('now', '-30 days')

    GROUP BY
        f.dep_airport,
        f.arr_airport
),

previous_30 AS (

    SELECT
        f.dep_airport,
        f.arr_airport,
        SUM(p.amount) AS revenue_previous

    FROM payment p

    JOIN booking b
        ON b.booking_id = p.booking_id

    JOIN flight f
        ON f.flight_id = b.flight_id

    WHERE p.paid_at >= DATETIME('now', '-60 days')
      AND p.paid_at < DATETIME('now', '-30 days')

    GROUP BY
        f.dep_airport,
        f.arr_airport
)

SELECT
    da.iata_code AS dep,
    aa.iata_code AS arr,

    ROUND(COALESCE(r.revenue_recent, 0), 2)
        AS revenue_last_30_days,

    ROUND(p.revenue_previous, 2)
        AS revenue_previous_30_days

FROM previous_30 p

LEFT JOIN recent_30 r
    ON r.dep_airport = p.dep_airport
   AND r.arr_airport = p.arr_airport

JOIN airport da
    ON da.airport_id = p.dep_airport

JOIN airport aa
    ON aa.airport_id = p.arr_airport

WHERE p.revenue_previous > 5000
  AND COALESCE(r.revenue_recent, 0) < 1000

ORDER BY p.revenue_previous DESC;
""")

results = cursor.fetchall()

print(f"Total routes with falling revenue: {len(results)}")

for row in results[:20]:
    print(row)




conn.close()