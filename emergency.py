import os
from db import get_emergency_contact
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

print(API_KEY)


def draft_emergency_message():
    emergency_contact = get_emergency_contact()
    print("SENDING MESSAGE TO:", emergency_contact)
