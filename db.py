import sqlite3

DB_NAME = "owner.db"
DB_TABLE_NAME = "owner"


def create_db():
    try:
        con = sqlite3.connect(DB_NAME)
        with con:
            cur = con.cursor()
            cur.execute(
                """CREATE TABLE IF NOT EXISTS owner (
                        username text,
                        password text,
                        email text,
                        first_name text,
                        last_name text,
                        emergency_contact integer
                )"""
            )
    except sqlite3.Error as error:
        print("Error connecting to SQLite database", error)


def insert_data(
    username: str,
    password: str,
    email: str,
    first_name: str,
    last_name: str,
    emergency_contact: int,
):
    con = sqlite3.connect(DB_NAME)
    with con:
        cur = con.cursor()
        cur.execute(
            f"""
            INSERT INTO {DB_TABLE_NAME} VALUES ("{username}", "{password}", "{email}", "{first_name}", "{last_name}", {emergency_contact})
        """
        )


def get_owner_info():
    db = sqlite3.connect(DB_NAME)
    cur = db.cursor()

    cur.execute("SELECT username, email, first_name, last_name FROM owner")
    info = cur.fetchall()
    for elm in info:
        print(elm)
    cur.close()


def get_emergency_contact():
    db = sqlite3.connect(DB_NAME)
    cur = db.cursor()

    cur.execute("SELECT emergency_contact FROM owner")
    emergency_contact = cur.fetchone()
    cur.close()
    return emergency_contact


def main():
    create_db()
    print(get_owner_info()[0])
    print(get_emergency_contact()[0])


main()
