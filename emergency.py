from db import get_emergency_contact


def draft_emergency_message():
    emergency_contact = get_emergency_contact()
    print("SENDING MESSAGE TO:", emergency_contact)
