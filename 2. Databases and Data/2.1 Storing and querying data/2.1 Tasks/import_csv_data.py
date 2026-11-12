import csv
import sqlite3
from pathlib import Path

DATABASE_FILE = "airport_booking.db"

conn = sqlite3.connect(DATABASE_FILE)
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

print("Connected to airport_booking.db")

# ==========================================
# CHECK REQUIRED CSV FILES
# ==========================================

required_files = [
    "airports.csv",
    "customers.csv",
    "flights.csv",
    "bookings.csv",
    "payments.csv"
]

missing_files = [
    file_name
    for file_name in required_files
    if not Path(file_name).exists()
]

if missing_files:
    print("The following CSV files are missing:")

    for file_name in missing_files:
        print(file_name)

    conn.close()
    raise SystemExit(
        "Move the missing files into the same folder as this Python file."
    )

print("All five CSV files were found.")

# ==========================================
# REMOVE OLD SAMPLE DATA
# ==========================================

print("Removing the old sample data...")

cursor.execute("DROP TRIGGER IF EXISTS trg_payment_quarantine;")

cursor.execute("DELETE FROM payment;")
cursor.execute("DELETE FROM booking;")
cursor.execute("DELETE FROM flight;")
cursor.execute("DELETE FROM customer;")
cursor.execute("DELETE FROM airport;")

cursor.execute("""
DELETE FROM sqlite_sequence
WHERE name IN (
    'airport',
    'customer',
    'flight',
    'booking',
    'payment'
);
""")

conn.commit()

print("Old sample data removed.")

# ==========================================
# CHECK PAYMENT TABLE SCHEMA
# ==========================================

cursor.execute("""
SELECT sql
FROM sqlite_master
WHERE type = 'table'
  AND name = 'payment';
""")

payment_table_result = cursor.fetchone()

if payment_table_result is None:
    conn.close()
    raise SystemExit("The payment table could not be found.")

payment_table_sql = payment_table_result[0]

if "BANK_TRANSFER" not in payment_table_sql:
    conn.close()
    raise SystemExit(
        "The payment table does not currently allow BANK_TRANSFER. "
        "Complete Step 8 before running the import."
    )

print("Payment table supports BANK_TRANSFER.")

# ==========================================
# CSV READER
# ==========================================

def read_csv(file_name):
    with open(
        file_name,
        mode="r",
        encoding="utf-8-sig",
        newline=""
    ) as csv_file:

        reader = csv.DictReader(csv_file)

        return list(reader)

    # ==========================================
# IMPORT AIRPORTS
# ==========================================

airport_rows = read_csv("airports.csv")

cursor.executemany("""
INSERT INTO airport (
    airport_id,
    iata_code,
    name,
    city,
    country,
    created_at
)
VALUES (
    :airport_id,
    :iata_code,
    :name,
    :city,
    :country,
    :created_at
);
""", airport_rows)

print(f"Imported {len(airport_rows)} airports.")

# ==========================================
# IMPORT CUSTOMERS
# ==========================================

customer_rows = read_csv("customers.csv")

cursor.executemany("""
INSERT INTO customer (
    customer_id,
    email,
    first_name,
    last_name,
    created_at,
    marketing_ok
)
VALUES (
    :customer_id,
    :email,
    :first_name,
    :last_name,
    :created_at,
    :marketing_ok
);
""", customer_rows)

print(f"Imported {len(customer_rows)} customers.")

# ==========================================
# IMPORT FLIGHTS
# ==========================================

flight_rows = read_csv("flights.csv")

cursor.executemany("""
INSERT INTO flight (
    flight_id,
    flight_no,
    dep_airport,
    arr_airport,
    dep_time,
    arr_time
)
VALUES (
    :flight_id,
    :flight_no,
    :dep_airport,
    :arr_airport,
    :dep_time,
    :arr_time
);
""", flight_rows)

print(f"Imported {len(flight_rows)} flights.")

# ==========================================
# IMPORT BOOKINGS
# ==========================================

booking_rows = read_csv("bookings.csv")

cursor.executemany("""
INSERT INTO booking (
    booking_id,
    customer_id,
    flight_id,
    booked_at,
    status,
    base_fare
)
VALUES (
    :booking_id,
    :customer_id,
    :flight_id,
    :booked_at,
    :status,
    :base_fare
);
""", booking_rows)

print(f"Imported {len(booking_rows)} bookings.")

# ==========================================
# IMPORT PAYMENTS
# ==========================================

payment_rows = read_csv("payments.csv")

cursor.executemany("""
INSERT INTO payment (
    payment_id,
    booking_id,
    paid_at,
    amount,
    method,
    currency
)
VALUES (
    :payment_id,
    :booking_id,
    :paid_at,
    :amount,
    :method,
    :currency
);
""", payment_rows)

print(f"Imported {len(payment_rows)} payments.")

# ==========================================
# SAVE IMPORT
# ==========================================

conn.commit()

print("All CSV records were committed to the database.")

# ==========================================
# FOREIGN KEY CHECK
# ==========================================

cursor.execute("PRAGMA foreign_key_check;")

foreign_key_errors = cursor.fetchall()

if foreign_key_errors:
    print("\nForeign-key problems were found:")

    for error in foreign_key_errors:
        print(error)
else:
    print("Foreign-key check passed.")

    # ==========================================
# VERIFY ROW COUNTS
# ==========================================

print("\n--- FINAL ROW COUNTS ---")

tables = [
    "airport",
    "customer",
    "flight",
    "booking",
    "payment"
]

for table_name in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
    row_count = cursor.fetchone()[0]

    print(f"{table_name}: {row_count}")