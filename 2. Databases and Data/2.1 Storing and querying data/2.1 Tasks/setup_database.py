import sqlite3

conn = sqlite3.connect("airport_booking.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

cursor.execute("""
CREATE TABLE IF NOT EXISTS airport (
    airport_id INTEGER PRIMARY KEY AUTOINCREMENT,
    iata_code CHAR(3) NOT NULL UNIQUE,
    name VARCHAR(200) NOT NULL,
    city VARCHAR(120) NOT NULL,
    country VARCHAR(120) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT (datetime('now'))
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS customer (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    first_name VARCHAR(120) NOT NULL,
    last_name VARCHAR(120) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT (datetime('now')),
    marketing_ok INTEGER NOT NULL DEFAULT 0
        CHECK(marketing_ok IN (0, 1))
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS flight (
    flight_id INTEGER PRIMARY KEY AUTOINCREMENT,
    flight_no VARCHAR(20) NOT NULL,
    dep_airport INTEGER NOT NULL REFERENCES airport(airport_id),
    arr_airport INTEGER NOT NULL REFERENCES airport(airport_id),
    dep_time DATETIME NOT NULL,
    arr_time DATETIME NOT NULL,
    CHECK(arr_time > dep_time),
    CHECK(dep_airport <> arr_airport)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS booking (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL REFERENCES customer(customer_id),
    flight_id INTEGER NOT NULL REFERENCES flight(flight_id),
    booked_at DATETIME NOT NULL DEFAULT (datetime('now')),
    status VARCHAR(20) NOT NULL
        CHECK(status IN ('PENDING', 'CONFIRMED', 'CANCELLED')),
    base_fare DECIMAL(10,2) NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS payment (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    booking_id INTEGER NOT NULL
        REFERENCES booking(booking_id) ON DELETE CASCADE,
    paid_at DATETIME NOT NULL DEFAULT (datetime('now')),
    amount DECIMAL(10,2) NOT NULL,
    method VARCHAR(20) NOT NULL
        CHECK(method IN ('CARD', 'PAYPAL', 'VOUCHER')),
    currency CHAR(3) NOT NULL
        CHECK(LENGTH(currency) = 3)
);
""")


cursor.execute("""
INSERT INTO airport (iata_code, name, city, country)
VALUES ('LHR', 'Heathrow', 'London', 'UK')
ON CONFLICT(iata_code) DO NOTHING;
""")

cursor.execute("""
INSERT INTO airport (iata_code, name, city, country)
VALUES ('JFK', 'John F. Kennedy', 'New York', 'USA')
ON CONFLICT(iata_code) DO NOTHING;
""")

cursor.execute("""
INSERT INTO customer (
    email,
    first_name,
    last_name,
    marketing_ok
)
VALUES (
    'ava@example.com',
    'Ava',
    'Singh',
    1
)
ON CONFLICT(email) DO NOTHING;
""")

cursor.execute("""
WITH dep AS (
    SELECT airport_id AS id
    FROM airport
    WHERE iata_code = 'LHR'
),
arr AS (
    SELECT airport_id AS id
    FROM airport
    WHERE iata_code = 'JFK'
)
INSERT INTO flight (
    flight_no,
    dep_airport,
    arr_airport,
    dep_time,
    arr_time
)
SELECT
    'TO101',
    dep.id,
    arr.id,
    datetime('now', '+3 days'),
    datetime('now', '+3 days', '+7 hours')
FROM dep, arr;
""")

cursor.execute("""
WITH c AS (
    SELECT customer_id
    FROM customer
    WHERE email = 'ava@example.com'
),
f AS (
    SELECT flight_id
    FROM flight
    WHERE flight_no = 'TO101'
    ORDER BY flight_id DESC
    LIMIT 1
)
INSERT INTO booking (
    customer_id,
    flight_id,
    status,
    base_fare
)
SELECT
    c.customer_id,
    f.flight_id,
    'CONFIRMED',
    450.00
FROM c, f;
""")

cursor.execute("""
INSERT INTO payment (
    booking_id,
    amount,
    method,
    currency
)
SELECT
    b.booking_id,
    450.00,
    'CARD',
    'GBP'
FROM booking b
JOIN customer c
    ON c.customer_id = b.customer_id
JOIN flight f
    ON f.flight_id = b.flight_id
WHERE c.email = 'ava@example.com'
  AND f.flight_no = 'TO101'
  AND NOT EXISTS (
      SELECT 1
      FROM payment p
      WHERE p.booking_id = b.booking_id
  );
""")

print("\n--- BOOKING TABLE STRUCTURE ---")

cursor.execute("PRAGMA table_info('booking');")

for row in cursor.fetchall():
    print(row)

print("\n--- PAYMENT FOREIGN KEYS ---")

cursor.execute("PRAGMA foreign_key_list('payment');")

for row in cursor.fetchall():
    print(row)

print("\n--- ALL TABLES ---")

cursor.execute("""
SELECT name
FROM sqlite_master
WHERE type = 'table'
AND name NOT LIKE 'sqlite_%'
ORDER BY name;
""")

for row in cursor.fetchall():
    print(row)

# =====================================================
# EXTENSION 1 - CREATE STAGING AND REJECT TABLES
# =====================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS raw_customer (
    email TEXT,
    first_name TEXT,
    last_name TEXT,
    created_at DATETIME,
    marketing_ok INTEGER
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS reject_customer (
    email TEXT,
    first_name TEXT,
    last_name TEXT,
    created_at DATETIME,
    marketing_ok INTEGER,
    reason TEXT NOT NULL,
    rejected_at DATETIME NOT NULL DEFAULT (datetime('now'))
);
""")

conn.commit()

# =====================================================
# EXTENSION 2 - ADD TEST DATA TO STAGING
# =====================================================

cursor.execute("DELETE FROM raw_customer;")
cursor.execute("DELETE FROM reject_customer;")

cursor.executemany("""
INSERT INTO raw_customer (
    email,
    first_name,
    last_name,
    marketing_ok
)
VALUES (?, ?, ?, ?);
""", [
    ("john@example.com", "John", "Smith", 1),
    ("bademail.com", "Sarah", "Jones", 0),
    ("peter@example.com", "", "Brown", 1),
    ("lucy@example.com", "Lucy", "Taylor", 0)
])

conn.commit()

# =====================================================
# EXTENSION 3 - QUARANTINE BAD DATA
# =====================================================

cursor.execute("""
INSERT INTO reject_customer (
    email,
    first_name,
    last_name,
    created_at,
    marketing_ok,
    reason
)
SELECT
    email,
    first_name,
    last_name,
    COALESCE(created_at, datetime('now')),
    CASE
        WHEN marketing_ok IN (0, 1) THEN marketing_ok
        ELSE 0
    END,
    CASE
        WHEN email NOT LIKE '%@%' THEN 'bad_email'
        WHEN IFNULL(first_name, '') = '' THEN 'missing_first_name'
        WHEN IFNULL(last_name, '') = '' THEN 'missing_last_name'
        ELSE 'unknown'
    END
FROM raw_customer
WHERE email NOT LIKE '%@%'
   OR IFNULL(first_name, '') = ''
   OR IFNULL(last_name, '') = '';
""")

conn.commit()

# =====================================================
# EXTENSION 4 - MOVE GOOD DATA INTO CUSTOMER
# =====================================================

cursor.execute("""
INSERT INTO customer (
    email,
    first_name,
    last_name,
    created_at,
    marketing_ok
)
SELECT
    email,
    first_name,
    last_name,
    COALESCE(created_at, datetime('now')),
    CASE
        WHEN marketing_ok IN (0, 1) THEN marketing_ok
        ELSE 0
    END
FROM raw_customer
WHERE email LIKE '%@%'
  AND IFNULL(first_name, '') <> ''
  AND IFNULL(last_name, '') <> ''
ON CONFLICT(email) DO NOTHING;
""")

conn.commit()

# =====================================================
# EXTENSION 5 - VIEW RESULTS
# =====================================================

print("\n--- VALID CUSTOMERS ---")

cursor.execute("""
SELECT email, first_name, last_name
FROM customer;
""")

for row in cursor.fetchall():
    print(row)


print("\n--- REJECTED CUSTOMERS ---")

cursor.execute("""
SELECT email, first_name, last_name, reason
FROM reject_customer;
""")

for row in cursor.fetchall():
    print(row)

# =====================================================
# EXTENSION 6 - CLEAR STAGING
# =====================================================

cursor.execute("""
DELETE FROM raw_customer;
""")

conn.commit()

# =====================================================
# EXTENSION 7 - PAYMENT QUARANTINE TABLE
# =====================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS reject_payment (
    booking_id INTEGER,
    paid_at DATETIME,
    amount REAL,
    method TEXT,
    currency TEXT,
    reason TEXT NOT NULL,
    rejected_at TEXT NOT NULL DEFAULT (datetime('now'))
);
""")

conn.commit()

# =====================================================
# EXTENSION 8 - PAYMENT VALIDATION TRIGGER
# =====================================================

cursor.execute("""
CREATE TRIGGER IF NOT EXISTS trg_payment_quarantine
BEFORE INSERT ON payment
WHEN NEW.amount = 0
   OR LENGTH(NEW.currency) <> 3
   OR NOT EXISTS (
       SELECT 1
       FROM booking b
       WHERE b.booking_id = NEW.booking_id
   )
BEGIN

    INSERT INTO reject_payment (
        booking_id,
        paid_at,
        amount,
        method,
        currency,
        reason
    )
    VALUES (
        NEW.booking_id,
        NEW.paid_at,
        NEW.amount,
        NEW.method,
        NEW.currency,
        CASE
            WHEN NEW.amount = 0 THEN 'zero_amount'
            WHEN LENGTH(NEW.currency) <> 3 THEN 'bad_currency'
            ELSE 'missing_booking'
        END
    );

    SELECT RAISE(IGNORE);

END;
""")

conn.commit()

# =====================================================
# EXTENSION 9 - TEST PAYMENT TRIGGER
# =====================================================

cursor.execute("""
INSERT INTO payment (
    booking_id,
    amount,
    method,
    currency
)
VALUES (
    999999,
    50.00,
    'CARD',
    'GBP'
);
""")

conn.commit()
print("\n--- REJECTED PAYMENTS ---")

cursor.execute("""
SELECT
    booking_id,
    amount,
    method,
    currency,
    reason
FROM reject_payment;
""")

for row in cursor.fetchall():
    print(row)

# =====================================================
# EXTENSION 11 - SAFE PAYMENT SCHEMA CHANGE
# =====================================================

cursor.execute("""
CREATE TABLE payment_new (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    booking_id INTEGER NOT NULL
        REFERENCES booking(booking_id) ON DELETE CASCADE,
    paid_at DATETIME NOT NULL DEFAULT (datetime('now')),
    amount REAL NOT NULL CHECK(amount <> 0),
    method VARCHAR(20) NOT NULL
        CHECK(method IN (
            'CARD',
            'PAYPAL',
            'VOUCHER',
            'BANK_TRANSFER'
        )),
    currency CHAR(3) NOT NULL
        DEFAULT 'GBP'
        CHECK(LENGTH(currency) = 3)
);
""")

cursor.execute("""
INSERT INTO payment_new (
    payment_id,
    booking_id,
    paid_at,
    amount,
    method,
    currency
)
SELECT
    payment_id,
    booking_id,
    paid_at,
    amount,
    method,
    COALESCE(NULLIF(currency, ''), 'GBP')
FROM payment;
""")

cursor.execute("""
DROP TABLE payment;
""")

cursor.execute("""
ALTER TABLE payment_new
RENAME TO payment;
""")

conn.commit()


conn.close()