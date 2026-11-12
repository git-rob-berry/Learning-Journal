import sqlite3

# ==========================================
# CONNECT TO DATABASE
# ==========================================

conn = sqlite3.connect("airport_booking.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")


# ==========================================
# CONSOLIDATION 1
# 10 MOST RECENT CUSTOMERS
# ==========================================

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

results = cursor.fetchall()

print(f"Results returned: {len(results)}")

for row in results:
    print(row)


# ==========================================
# CONSOLIDATION 2
# LHR FLIGHTS IN NEXT 14 DAYS
# ==========================================

print("\n--- LHR FLIGHTS NEXT 14 DAYS ---")

# First count ALL matching flights
cursor.execute("""
SELECT COUNT(*)
FROM flight f
JOIN airport a
    ON f.dep_airport = a.airport_id
WHERE a.iata_code = 'LHR'
  AND f.dep_time BETWEEN datetime('now')
                     AND datetime('now', '+14 days');
""")

total = cursor.fetchone()[0]

print(f"Total matching flights: {total}")
print("Showing first 20:")

# Now display only the first 20
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
ORDER BY f.dep_time
LIMIT 20;
""")

for row in cursor.fetchall():
    print(row)


# ==========================================
# CONSOLIDATION 3
# UNPAID BOOKINGS
# ==========================================

print("\n--- UNPAID BOOKINGS ---")

# Run the full query first so we know
# how many unpaid bookings exist
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

results = cursor.fetchall()

print(f"Total unpaid bookings: {len(results)}")
print("Showing first 20:")

for row in results[:20]:
    print(row)


# ==========================================
# CONSOLIDATION 4
# GMAIL AND OUTLOOK CUSTOMERS
# ==========================================

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

results = cursor.fetchall()

print(f"Total matching customers: {len(results)}")
print("Showing first 20:")

for row in results[:20]:
    print(row)


# ==========================================
# EXTENSION 1
# BOOKING SUMMARY
# ==========================================

print("\n--- BOOKING SUMMARY ---")

# Count the total number of bookings
cursor.execute("""
SELECT COUNT(*)
FROM booking;
""")

total = cursor.fetchone()[0]

print(f"Total bookings: {total}")
print("Showing first 20:")

# Display only 20 booking summaries
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

ORDER BY b.booked_at DESC
LIMIT 20;
""")

for row in cursor.fetchall():
    print(row)


# ==========================================
# EXTENSION 2
# DUPLICATE EMAIL CHECK
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

print(f"Duplicate email addresses found: {len(results)}")

if results:

    print("Showing first 20:")

    for row in results[:20]:
        print(row)

else:
    print("No duplicate emails found.")


# ==========================================
# EXTENSION 3
# BOOKING STATUS DISTRIBUTION
# ==========================================

print("\n--- BOOKING STATUS DISTRIBUTION ---")

cursor.execute("""
SELECT
    status,
    COUNT(*) AS bookings
FROM booking
GROUP BY status
ORDER BY bookings DESC;
""")

results = cursor.fetchall()

for row in results:
    print(row)

# Also print the total number of bookings
total_bookings = sum(row[1] for row in results)

print(f"Total bookings: {total_bookings}")


# ==========================================
# EXTENSION 4
# PAYMENT VS BASE FARE CHECK
# ==========================================

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

print(f"Bookings where payments do not match base fare: {len(results)}")

if results:

    print("Showing first 20:")

    for row in results[:20]:
        print(row)

else:
    print("All booking payments match their base fares.")


# ==========================================
# CLOSE DATABASE
# ==========================================

conn.close()

print("\n--- ALL QUERIES COMPLETE ---")