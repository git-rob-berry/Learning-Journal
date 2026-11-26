import sqlite3

# ==========================================
# CONNECT TO THE EXISTING DATABASE
# ==========================================

conn = sqlite3.connect("airport_booking.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

print("Connected to airport_booking.db")

# M2T4 code will go below this line

# ==========================================
# 1A - CREATE BOOKING FACTS VIEW
# ==========================================

cursor.execute("""
CREATE VIEW IF NOT EXISTS v_booking_facts AS

SELECT
    b.booking_id,
    b.booked_at,
    b.status,
    b.base_fare,
    c.email,
    f.flight_no,
    da.iata_code AS dep,
    aa.iata_code AS arr

FROM booking b

JOIN customer c
    ON c.customer_id = b.customer_id

JOIN flight f
    ON f.flight_id = b.flight_id

JOIN airport da
    ON da.airport_id = f.dep_airport

JOIN airport aa
    ON aa.airport_id = f.arr_airport;
""")

print("Created v_booking_facts.")

print("\n--- BOOKING FACTS VIEW ---")

cursor.execute("""
SELECT *
FROM v_booking_facts
ORDER BY booked_at DESC
LIMIT 5;
""")

for row in cursor.fetchall():
    print(row)

# ==========================================
# 1C - CREATE BOOKING WITH PAID VIEW
# ==========================================

cursor.execute("""
CREATE VIEW IF NOT EXISTS v_booking_with_paid AS

SELECT
    b.*,

    COALESCE(
        (
            SELECT SUM(p.amount)
            FROM payment p
            WHERE p.booking_id = b.booking_id
        ),
        0
    ) AS total_paid

FROM booking b;
""")

print("Created v_booking_with_paid.")

print("\n--- BOOKING WITH PAID VIEW ---")

cursor.execute("""
SELECT
    booking_id,
    status,
    base_fare,
    total_paid
FROM v_booking_with_paid
ORDER BY booked_at DESC
LIMIT 5;
""")

for row in cursor.fetchall():
    print(row)

# ==========================================
# 2A - CREATE MONTHLY REVENUE TABLE
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS mv_monthly_revenue (
    month_start TEXT PRIMARY KEY,
    revenue REAL NOT NULL
);
""")

print("Created mv_monthly_revenue.")

# ==========================================
# 2B - REFRESH MONTHLY REVENUE
# ==========================================

try:
    cursor.execute("BEGIN TRANSACTION;")

    cursor.execute("""
    DELETE FROM mv_monthly_revenue;
    """)

    cursor.execute("""
    INSERT INTO mv_monthly_revenue (
        month_start,
        revenue
    )

    SELECT
        DATE(strftime('%Y-%m-01', paid_at)) AS month_start,
        ROUND(SUM(amount), 2) AS revenue

    FROM payment

    GROUP BY month_start;
    """)

    conn.commit()

    print("Monthly revenue refreshed successfully.")

except sqlite3.Error as error:
    conn.rollback()

    print("Monthly revenue refresh failed:")
    print(error)

print("\n--- MONTHLY REVENUE ---")

cursor.execute("""
SELECT
    month_start,
    revenue
FROM mv_monthly_revenue
ORDER BY month_start DESC
LIMIT 10;
""")

for row in cursor.fetchall():
    print(row)

# ==========================================
# 3A - CREATE INDEXES
# ==========================================

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_booking_cust_time
ON booking (
    customer_id,
    booked_at DESC
);
""")

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_payment_booking_time
ON payment (
    booking_id,
    paid_at DESC
);
""")

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_flight_dep_time
ON flight (
    dep_airport,
    dep_time
);
""")

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_booking_confirmed_recent
ON booking (
    booked_at
)
WHERE status = 'CONFIRMED';
""")

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_payment_month
ON payment (
    DATE(strftime('%Y-%m-01', paid_at))
);
""")

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_pay_cover
ON payment (
    booking_id,
    amount,
    paid_at
);
""")

conn.commit()

print("M2T4 indexes created.")

# ==========================================
# 4A - EXPLAIN A FLIGHT QUERY
# ==========================================

print("\n--- FLIGHT QUERY PLAN ---")

cursor.execute("""
EXPLAIN QUERY PLAN

SELECT
    flight_id,
    flight_no,
    dep_time
FROM flight
WHERE dep_airport = 1
ORDER BY dep_time;
""")

for row in cursor.fetchall():
    print(row)

# ==========================================
# 4B - UPDATE QUERY PLANNER INFORMATION
# ==========================================

cursor.execute("ANALYZE;")
cursor.execute("PRAGMA optimize;")

conn.commit()

print("ANALYZE and PRAGMA optimize completed.")

# ==========================================
# 5 - RUNNING REVENUE PER CUSTOMER
# ==========================================

print("\n--- RUNNING REVENUE PER CUSTOMER ---")

cursor.execute("""
SELECT
    c.customer_id,
    c.email,
    p.paid_at,
    p.amount,

    ROUND(
        SUM(p.amount) OVER (
            PARTITION BY c.customer_id
            ORDER BY p.paid_at, p.payment_id
            ROWS BETWEEN UNBOUNDED PRECEDING
                     AND CURRENT ROW
        ),
        2
    ) AS running_revenue

FROM customer c

JOIN booking b
    ON b.customer_id = c.customer_id

JOIN payment p
    ON p.booking_id = b.booking_id

ORDER BY
    c.customer_id,
    p.paid_at,
    p.payment_id

LIMIT 20;
""")

for row in cursor.fetchall():
    print(row)

# ==========================================
# 6 - DAYS SINCE PREVIOUS BOOKING
# ==========================================

print("\n--- DAYS SINCE PREVIOUS BOOKING ---")

cursor.execute("""
SELECT
    b.customer_id,
    b.booking_id,
    b.booked_at,

    ROUND(
        (
            strftime('%s', b.booked_at)
            -
            strftime(
                '%s',

                LAG(b.booked_at) OVER (
                    PARTITION BY b.customer_id
                    ORDER BY b.booked_at, b.booking_id
                )
            )
        ) / 86400.0,
        1
    ) AS days_since_previous

FROM booking b

ORDER BY
    b.customer_id,
    b.booked_at,
    b.booking_id

LIMIT 20;
""")

for row in cursor.fetchall():
    print(row)

# ==========================================
# 7 - ROUTE REVENUE LEADERBOARD
# ==========================================

print("\n--- ROUTE REVENUE LEADERBOARD - LAST 30 DAYS ---")

cursor.execute("""
WITH route_revenue AS (

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
)

SELECT
    dep,
    arr,
    revenue_30d,

    RANK() OVER (
        ORDER BY revenue_30d DESC
    ) AS revenue_rank

FROM route_revenue

ORDER BY revenue_rank

LIMIT 20;
""")

results = cursor.fetchall()

print(f"Routes found: {len(results)}")

for row in results:
    print(row)

# ==========================================
# CONSOLIDATION 1
# TOP 10 ROUTES BY RECENT REVENUE
# ==========================================

print("\n--- TOP 10 ROUTES BY 30-DAY REVENUE ---")

cursor.execute("""
WITH payment_per_booking AS (

    SELECT
        booking_id,
        SUM(amount) AS total_paid

    FROM payment

    WHERE paid_at >= DATETIME('now', '-30 days')

    GROUP BY booking_id
)

SELECT
    da.iata_code AS dep,
    aa.iata_code AS arr,

    ROUND(
        SUM(ppb.total_paid),
        2
    ) AS revenue_30d

FROM payment_per_booking ppb

JOIN booking b
    ON b.booking_id = ppb.booking_id

JOIN flight f
    ON f.flight_id = b.flight_id

JOIN airport da
    ON da.airport_id = f.dep_airport

JOIN airport aa
    ON aa.airport_id = f.arr_airport

GROUP BY
    da.iata_code,
    aa.iata_code

ORDER BY revenue_30d DESC

LIMIT 10;
""")

results = cursor.fetchall()

print(f"Routes returned: {len(results)}")

for row in results:
    print(row)

# ==========================================
# CONSOLIDATION 2
# UNPAID OR PARTIALLY PAID CONFIRMED BOOKINGS
# ==========================================

print("\n--- UNPAID OR PARTIALLY PAID CONFIRMED BOOKINGS ---")

cursor.execute("""
WITH payment_totals AS (

    SELECT
        booking_id,
        SUM(amount) AS total_paid

    FROM payment

    GROUP BY booking_id
)

SELECT
    b.booking_id,
    c.email,
    b.base_fare,

    ROUND(
        COALESCE(pt.total_paid, 0),
        2
    ) AS total_paid,

    ROUND(
        b.base_fare - COALESCE(pt.total_paid, 0),
        2
    ) AS outstanding

FROM booking b

JOIN customer c
    ON c.customer_id = b.customer_id

LEFT JOIN payment_totals pt
    ON pt.booking_id = b.booking_id

WHERE b.status = 'CONFIRMED'

  AND COALESCE(pt.total_paid, 0) < b.base_fare

ORDER BY outstanding DESC;
""")

results = cursor.fetchall()

print(f"Total matching bookings: {len(results)}")
print("Showing first 20:")

for row in results[:20]:
    print(row)

# ==========================================
# CONSOLIDATION 3
# MONTHLY BOOKING MIX
# ==========================================

print("\n--- MONTHLY BOOKING MIX ---")

cursor.execute("""
SELECT
    DATE(strftime('%Y-%m-01', booked_at)) AS month_start,

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
# CONSOLIDATION 4A
# RUNNING CUSTOMER REVENUE
# ==========================================

print("\n--- RUNNING CUSTOMER REVENUE ---")

cursor.execute("""
SELECT
    c.customer_id,
    c.email,
    p.payment_id,
    p.paid_at,
    p.amount,

    ROUND(
        SUM(p.amount) OVER (
            PARTITION BY c.customer_id
            ORDER BY p.paid_at, p.payment_id
            ROWS BETWEEN UNBOUNDED PRECEDING
                     AND CURRENT ROW
        ),
        2
    ) AS running_revenue

FROM customer c

JOIN booking b
    ON b.customer_id = c.customer_id

JOIN payment p
    ON p.booking_id = b.booking_id

ORDER BY
    c.customer_id,
    p.paid_at,
    p.payment_id;
""")

results = cursor.fetchall()

print(f"Total payment records: {len(results)}")
print("Showing first 20:")

for row in results[:20]:
    print(row)

# ==========================================
# CONSOLIDATION 4B
# DAYS SINCE PREVIOUS BOOKING
# ==========================================

print("\n--- BOOKING RECENCY GAP ---")

cursor.execute("""
WITH booking_history AS (

    SELECT
        b.customer_id,
        b.booking_id,
        b.booked_at,

        LAG(b.booked_at) OVER (
            PARTITION BY b.customer_id
            ORDER BY b.booked_at, b.booking_id
        ) AS previous_booking_at

    FROM booking b
)

SELECT
    customer_id,
    booking_id,
    booked_at,
    previous_booking_at,

    ROUND(
        (
            strftime('%s', booked_at)
            -
            strftime('%s', previous_booking_at)
        ) / 86400.0,
        1
    ) AS days_since_previous

FROM booking_history

ORDER BY
    customer_id,
    booked_at,
    booking_id;
""")

results = cursor.fetchall()

print(f"Total booking records: {len(results)}")
print("Showing first 20:")

for row in results[:20]:
    print(row)

# ==========================================
# CONSOLIDATION 5A
# REMOVE DEMO INDEX FOR A CLEAN TEST
# ==========================================

cursor.execute("""
DROP INDEX IF EXISTS idx_payment_paid_at;
""")

conn.commit()

print("\n--- QUERY PLAN BEFORE PAID_AT INDEX ---")

cursor.execute("""
EXPLAIN QUERY PLAN

SELECT
    payment_id,
    booking_id,
    paid_at,
    amount
FROM payment
WHERE paid_at >= '2025-01-01'
  AND paid_at < '2026-01-01'
ORDER BY paid_at;
""")

before_plan = cursor.fetchall()

for row in before_plan:
    print(row)

# ==========================================
# CONSOLIDATION 5C
# ADD TARGETED INDEX
# ==========================================

cursor.execute("""
CREATE INDEX idx_payment_paid_at
ON payment (
    paid_at
);
""")

cursor.execute("ANALYZE;")
cursor.execute("PRAGMA optimize;")

conn.commit()

print("Created idx_payment_paid_at.")

print("\n--- QUERY PLAN AFTER PAID_AT INDEX ---")

cursor.execute("""
EXPLAIN QUERY PLAN

SELECT
    payment_id,
    booking_id,
    paid_at,
    amount
FROM payment
WHERE paid_at >= '2025-01-01'
  AND paid_at < '2026-01-01'
ORDER BY paid_at;
""")

after_plan = cursor.fetchall()

for row in after_plan:
    print(row)

print("\n--- INDEX PLAN COMPARISON ---")

print("Before index:")

for row in before_plan:
    print(row)

print("\nAfter index:")

for row in after_plan:
    print(row)




conn.close()

print("\n--- ALL M2T4 TASKS COMPLETE ---")