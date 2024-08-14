import db


def send_emergency_message():
    """Create and send an emergency message to the owner's emergency contact."""

    def get_info(getter_func, error_message):
        try:
            return getter_func()
        except Exception as e:
            print(f"{error_message}: {e}")
            return None

    username, email, first_name, last_name = get_info(
        db.get_owner_info, "Unable to retrieve owner information"
    )
    emergency_contact = get_info(
        db.get_emergency_contact, "Unable to retrieve emergency contact"
    )
    carrier = get_info(db.get_carrier, "Unable to retrieve emergency contact carrier")

    # Construct the message and add some metadata
    message = (
        "This is an emergency notification from FallBot. The device owner "
        f"{first_name} {last_name}, has experienced a fall and has remained "
        "down for an unusual amount of time. Immediate assistance may be "
        "required.\nPlease contact emergency services right away."
    )
    metadata = {
        "owner_username": username,
        "owner_email": email,
        "recipient_contact_info": emergency_contact,
        "recipient_carrier": carrier,
    }

    print("\n\n")
    print(message, "\n")
    print(metadata, "\n\n")
