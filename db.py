import sqlite3

DB_NAME = "owner.db"
DB_TABLE_NAME = "owner"


def create_owner_database():
    """Create the database. Needs to only be run once."""
    try:
        with sqlite3.connect(DB_NAME) as con:
            cur = con.cursor()
            query = f"""
            CREATE TABLE IF NOT EXISTS {DB_TABLE_NAME} (
                username text,
                email text,
                first_name text,
                last_name text,
                emergency_contact integer
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
):
    """Insert the owner information into the database."""
    with sqlite3.connect(DB_NAME) as con:
        cur = con.cursor()
        query = f"""
        INSERT INTO {DB_TABLE_NAME} (
            username, email, first_name, last_name, emergency_contact
        ) VALUES (?, ?, ?, ?, ?)"""
        cur.execute(query, (username, email, first_name, last_name, emergency_contact))
        con.commit()


def get_owner_info():
    """Retrieve the username, email, first name, and last name of the owner."""
    owner_info = []
    with sqlite3.connect(DB_NAME) as con:
        cur = con.cursor()
        query = f"SELECT username, email, first_name, last_name FROM {DB_TABLE_NAME}"
        cur.execute(query)
        owner_info = cur.fetchone()
    return owner_info


def get_emergency_contact():
    """Retrieve the emergency contact from the owner table."""
    with sqlite3.connect(DB_NAME) as con:
        cur = con.cursor()
        query = f"SELECT emergency_contact FROM {DB_TABLE_NAME}"
        cur.execute(query)
        emergency_contact = cur.fetchone()
    return emergency_contact


def main():
    create_owner_database()
    print(get_owner_info())
    print(get_emergency_contact()[0])


main()
