import sqlite3

conn = sqlite3.connect("airport_booking.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

print("\n--- AIRPORTS ---")

cursor.execute("SELECT * FROM airport;")

for row in cursor.fetchall():
    print(row)


print("\n--- CUSTOMERS ---")

cursor.execute("SELECT * FROM customer;")

for row in cursor.fetchall():
    print(row)


print("\n--- FLIGHTS ---")

cursor.execute("SELECT * FROM flight;")

for row in cursor.fetchall():
    print(row)


print("\n--- BOOKINGS ---")

cursor.execute("SELECT * FROM booking;")

for row in cursor.fetchall():
    print(row)


print("\n--- PAYMENTS ---")

cursor.execute("SELECT * FROM payment;")

for row in cursor.fetchall():
    print(row)


print("\n--- CUSTOMER LIST ---")

cursor.execute("""
SELECT
    customer_id AS id,
    first_name || ' ' || last_name AS full_name,
    email,
    created_at
FROM customer
ORDER BY created_at DESC;
""")

for row in cursor.fetchall():
    print(row)

print("\n--- UNIQUE AIRPORT LOCATIONS ---")

cursor.execute("""
SELECT DISTINCT
    city AS departure_city,
    country
FROM airport
ORDER BY country, departure_city;
""")

for row in cursor.fetchall():
    print(row)


print("\n--- RECENT MARKETING CUSTOMERS ---")

cursor.execute("""
SELECT
    customer_id,
    email,
    created_at
FROM customer
WHERE marketing_ok = 1
  AND created_at >= datetime('now', '-30 days')
ORDER BY created_at DESC;
""")

for row in cursor.fetchall():
    print(row)


print("\n--- UK OR USA AIRPORTS ---")

cursor.execute("""
SELECT
    iata_code,
    city,
    country
FROM airport
WHERE country IN ('UK', 'USA')
ORDER BY country, city;
""")

for row in cursor.fetchall():
    print(row)


print("\n--- CUSTOMER 1 RECENT BOOKINGS ---")

cursor.execute("""
SELECT
    booking_id,
    booked_at,
    status,
    base_fare
FROM booking
WHERE customer_id = 1
  AND booked_at BETWEEN datetime('now', '-90 days')
                    AND datetime('now')
ORDER BY booked_at DESC;
""")

for row in cursor.fetchall():
    print(row)


print("\n--- PAYMENTS WITH MISSING CURRENCY ---")

cursor.execute("""
SELECT *
FROM payment
WHERE currency IS NULL;
""")

for row in cursor.fetchall():
    print(row)

print("\n--- EXAMPLE.COM CUSTOMERS ---")

cursor.execute("""
SELECT
    customer_id,
    email
FROM customer
WHERE email LIKE '%@example.com';
""")

for row in cursor.fetchall():
    print(row)

print("\n--- TO FLIGHT NUMBERS ---")

cursor.execute("""
SELECT flight_no
FROM flight
WHERE flight_no GLOB 'TO[0-9][0-9][0-9]';
""")

for row in cursor.fetchall():
    print(row)

print("\n--- NEWEST BOOKINGS ---")

cursor.execute("""
SELECT
    booking_id,
    customer_id,
    booked_at,
    status
FROM booking
ORDER BY booked_at DESC, booking_id DESC
LIMIT 20;
""")

for row in cursor.fetchall():
    print(row)


print("\n--- BOOKINGS PAGE 2 ---")

cursor.execute("""
SELECT
    booking_id,
    customer_id,
    booked_at,
    status
FROM booking
ORDER BY booked_at DESC, booking_id DESC
LIMIT 20 OFFSET 20;
""")

for row in cursor.fetchall():
    print(row)

print("\n--- UPCOMING FLIGHTS ---")

cursor.execute("""
SELECT
    flight_no,
    dep_time,
    arr_time,
    ROUND(
        (julianday(arr_time) - julianday(dep_time)) * 24 * 60
    ) AS duration_minutes
FROM flight
WHERE dep_time BETWEEN datetime('now')
                   AND datetime('now', '+7 days')
ORDER BY dep_time;
""")

for row in cursor.fetchall():
    print(row)


print("\n--- 10 MOST RECENT CUSTOMERS ---")

cursor.execute("""
SELECT
    first_name || ' ' || last_name AS full_name,
    email,
    CAST(
        julianday('now') - julianday(created_at)
        AS INTEGER
    ) AS days_since_joining
FROM customer
ORDER BY created_at DESC
LIMIT 10;
""")

for row in cursor.fetchall():
    print(row)


print("\n--- LHR FLIGHTS NEXT 14 DAYS ---")

cursor.execute("""
SELECT
    f.flight_no,
    strftime('%Y-%m-%d', f.dep_time) AS dep_date,
    ROUND(
        (julianday(f.arr_time) - julianday(f.dep_time))
        * 24 * 60
    ) AS duration_minutes
FROM flight f
JOIN airport a
    ON f.dep_airport = a.airport_id
WHERE a.iata_code = 'LHR'
  AND f.dep_time BETWEEN datetime('now')
                     AND datetime('now', '+14 days')
ORDER BY f.dep_time;
""")

for row in cursor.fetchall():
    print(row)

print("\n--- UNPAID BOOKINGS ---")

cursor.execute("""
SELECT
    b.booking_id,
    c.email,
    f.flight_no,
    CAST(
        julianday('now') - julianday(b.booked_at)
        AS INTEGER
    ) AS days_since_booking,
    COALESCE(SUM(p.amount), 0) AS total_paid
FROM booking b
JOIN customer c
    ON b.customer_id = c.customer_id
JOIN flight f
    ON b.flight_id = f.flight_id
LEFT JOIN payment p
    ON b.booking_id = p.booking_id
GROUP BY
    b.booking_id,
    c.email,
    f.flight_no,
    b.booked_at
HAVING COALESCE(SUM(p.amount), 0) = 0;
""")

for row in cursor.fetchall():
    print(row)

print("\n--- GMAIL AND OUTLOOK CUSTOMERS ---")

cursor.execute("""
SELECT
    customer_id,
    first_name,
    last_name,
    email
FROM customer
WHERE email LIKE '%@gmail.com'
   OR email LIKE '%@outlook.com'
ORDER BY last_name, first_name;
""")

for row in cursor.fetchall():
    print(row)


# ==========================================
# EXTENSION 1 - BOOKING SUMMARY
# ==========================================

print("\n--- BOOKING SUMMARY ---")

cursor.execute("""
SELECT
    b.booking_id,
    c.first_name || ' ' || c.last_name AS customer,
    b.base_fare,

    IFNULL(
        (
            SELECT SUM(p.amount)
            FROM payment p
            WHERE p.booking_id = b.booking_id
        ),
        0
    ) AS total_paid,

    CASE b.status
        WHEN 'CONFIRMED' THEN 'Booked'
        WHEN 'PENDING' THEN 'Awaiting Payment'
        ELSE 'Cancelled'
    END AS status_label

FROM booking b

JOIN customer c
    ON c.customer_id = b.customer_id

ORDER BY b.booked_at DESC;
""")

for row in cursor.fetchall():
    print(row)



# ==========================================
# EXTENSION 2 - DATA QUALITY CHECKS
# ==========================================

print("\n--- DUPLICATE EMAIL CHECK ---")

cursor.execute("""
SELECT
    email,
    COUNT(*) AS count
FROM customer
GROUP BY email
HAVING COUNT(*) > 1;
""")

results = cursor.fetchall()

if results:
    for row in results:
        print(row)
else:
    print("No duplicate emails found.")

print("\n--- BOOKING STATUS DISTRIBUTION ---")

cursor.execute("""
SELECT
    status,
    COUNT(*) AS bookings
FROM booking
GROUP BY status;
""")

for row in cursor.fetchall():
    print(row)

print("\n--- PAYMENT VS BASE FARE CHECK ---")

cursor.execute("""
SELECT
    b.booking_id,
    b.base_fare,
    IFNULL(SUM(p.amount), 0) AS total_paid

FROM booking b

LEFT JOIN payment p
    ON p.booking_id = b.booking_id

GROUP BY
    b.booking_id,
    b.base_fare

HAVING IFNULL(SUM(p.amount), 0) <> b.base_fare;
""")

results = cursor.fetchall()

if results:
    for row in results:
        print(row)
else:
    print("All booking payments match their base fares.")

conn.close()