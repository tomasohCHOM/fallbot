import db
import os
import fall

if __name__ == "__main__":
    if not os.path.exists(db.DB_PATH):
        db.create_owner_database()
        username = input("Please enter your username: ")
        email = input("Please enter your email: ")
        first_name = input("Please enter your first name: ")
        last_name = input("Please enter your last name: ")
        emergency_contact = int(input("Please enter the emergency contact number: "))
        carrier = input(
            "Please enter the carrier associated with the emergency number: "
        )

        db.insert_data(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            emergency_contact=emergency_contact,
            carrier=carrier,
        )
    fall.run()
