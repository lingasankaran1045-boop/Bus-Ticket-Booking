import sqlite3

conn = sqlite3.connect("bus_booking.db")
cursor = conn.cursor()


def create_tables():

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS buses(
        bus_id TEXT PRIMARY KEY,
        bus_name TEXT,
        source TEXT,
        destination TEXT,
        departure_time TEXT,
        total_seats INTEGER,
        price REAL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        user_id TEXT PRIMARY KEY,
        name TEXT,
        age INTEGER,
        mobile_number TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bookings(
        booking_id TEXT PRIMARY KEY,
        user_id TEXT,
        bus_id TEXT,
        journey_date TEXT,
        seats INTEGER
    )
    """)

    conn.commit()


# ---------------- BUS ---------------- #

def add_bus_db(
        bus_id,
        bus_name,
        source,
        destination,
        departure_time,
        total_seats,
        price):

    cursor.execute("""
    INSERT INTO buses
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        bus_id,
        bus_name,
        source,
        destination,
        departure_time,
        total_seats,
        price
    ))

    conn.commit()


def get_all_buses():

    cursor.execute("SELECT * FROM buses")

    return cursor.fetchall()


def update_bus_db(bus_id, available_seats):

    cursor.execute("""
    UPDATE buses
    SET total_seats = ?
    WHERE bus_id = ?
    """, (
        available_seats,
        bus_id
    ))

    conn.commit()


def delete_bus_db(bus_id):

    cursor.execute("""
    DELETE FROM buses
    WHERE bus_id = ?
    """, (bus_id,))

    conn.commit()


# ---------------- USER ---------------- #

def register_user_db(
        user_id,
        name,
        age,
        mobile_number):

    cursor.execute("""
    INSERT INTO users
    VALUES (?, ?, ?, ?)
    """, (
        user_id,
        name,
        age,
        mobile_number
    ))

    conn.commit()


def get_user_details_db(user_id):

    cursor.execute("""
    SELECT * FROM users
    WHERE user_id = ?
    """, (user_id,))

    return cursor.fetchone()


# ---------------- BOOKING ---------------- #

def search_bus_db(source, destination):

    cursor.execute("""
    SELECT * FROM buses
    WHERE source = ?
    AND destination = ?
    """, (
        source,
        destination
    ))

    return cursor.fetchall()


def book_ticket_db(
        booking_id,
        user_id,
        bus_id,
        journey_date,
        seats,
        ):

    cursor.execute("""
    INSERT INTO bookings
    VALUES (?, ?, ?, ?, ?)
    """, (
        booking_id,
        user_id,
        bus_id,
        journey_date,
        seats
    ))

    cursor.execute("""
    UPDATE buses
    SET total_seats = total_seats - ?
    WHERE bus_id = ?
    """, (
        seats,
        bus_id
    ))

    conn.commit()


def cancel_ticket_db(booking_id):

    cursor.execute("""
    SELECT bus_id, seats
    FROM bookings
    WHERE booking_id = ?
    """, (booking_id,))

    booking = cursor.fetchone()

    if not booking:
        print("Booking not found!")
        return

    bus_id = booking[0]
    seats = booking[1]

    cursor.execute("""
    UPDATE buses
    SET total_seats = total_seats + ?
    WHERE bus_id = ?
    """, (
        seats,
        bus_id
    ))

    cursor.execute("""
    DELETE FROM bookings
    WHERE booking_id = ?
    """, (booking_id,))

    conn.commit()



def get_user_booking_db(user_id):

    cursor.execute("""
    SELECT * FROM bookings
    WHERE user_id = ?
    """, (user_id,))

    return cursor.fetchall()


def get_available_seats_db(bus_id):

    cursor.execute("""
    SELECT total_seats
    FROM buses
    WHERE bus_id = ?
    """, (bus_id,))

    result = cursor.fetchone()

    if result:
        return result[0]

    return 0