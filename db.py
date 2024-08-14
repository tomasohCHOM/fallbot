import sqlite3

DB_PATH = "owner.db"
DB_TABLE_NAME = "owner"


def create_owner_database():
    """Create the database. Needs to only be run once."""
    try:
        with sqlite3.connect(DB_PATH) as con:
            cur = con.cursor()
            query = f"""
            CREATE TABLE IF NOT EXISTS {DB_TABLE_NAME} (
                username text,
                email text,
                first_name text,
                last_name text,
                emergency_contact integer,
                carrier text
            )
            """
            cur.execute(query)
    except sqlite3.Error as error:
        print("Error connecting to SQLite database", error)


def insert_data(
    username: str,
    email: str,
    first_name: str,
    last_name: str,
    emergency_contact: int,
    carrier: str,
):
    """Insert the owner information into the database."""
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        query = f"""
        INSERT INTO {DB_TABLE_NAME} (
            username, email, first_name, last_name, emergency_contact, carrier
        ) VALUES (?, ?, ?, ?, ?, ?)"""
        cur.execute(
            query, (username, email, first_name, last_name, emergency_contact, carrier)
        )
        con.commit()


def clear_table():
    """Clear the owner table."""
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        query = f" DELETE FROM {DB_TABLE_NAME}"
        cur.execute(query)
        con.commit()


def get_owner_info():
    """Retrieve the username, email, first name, and last name of the owner."""
    owner_info = []
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        query = f"SELECT username, email, first_name, last_name FROM {DB_TABLE_NAME}"
        cur.execute(query)
        owner_info = cur.fetchone()
    if not owner_info:
        raise Exception("No owner information in DB.")
    return owner_info


def get_emergency_contact():
    """Retrieve the emergency contact from the owner table."""
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        query = f"SELECT emergency_contact FROM {DB_TABLE_NAME}"
        cur.execute(query)
        emergency_contact = cur.fetchone()
    if not emergency_contact:
        raise Exception("Could not get emergency contact in DB.")
    return emergency_contact[0] if emergency_contact else ""


def get_carrier():
    """Retrieve the carrier of the emergency contact from the owner table."""
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        query = f"SELECT carrier FROM {DB_TABLE_NAME}"
        cur.execute(query)
        carrier = cur.fetchone()
    if not carrier:
        raise Exception("Could not get carrier in DB.")
    return carrier[0]


def sample():
    # insert_data("maar", "mary@gmail.com", "mar", "nsh", 8492, "tmobile")
    print(get_emergency_contact())
    print(get_owner_info())
    print(get_carrier())
