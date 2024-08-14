import os
import db
from dotenv import load_dotenv

load_dotenv()


def send_emergency_message():
    emergency_contact = db.get_emergency_contact()
    print("SENDING MESSAGE TO:", emergency_contact)
