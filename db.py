import sqlite3


def create_db():

    db = sqlite3.connect("owner.db")
    cur = db.cursor()

    cur.execute(""" CREATE TABLE owner (
                username text,
                password text,
                email text,
                first_name text,
                last_name text,
                emergency_contact integer
    )""")
    db.close

def get_owner_info():
    db = sqlite3.connect("owner.db")
    cur = db.cursor()

    cur.execute("SELECT username, email, first_name, last_name")
    info = cur.fetchall()
    for elm in info:
        print(elm)
    cur.close()

def get_emergency_contact():
    db = sqlite3.connect("owner.db")
    cur = db.cursor()

    cur.execute("SELECT emergency_contact")
    return cur.fetchone()
    cur.close()