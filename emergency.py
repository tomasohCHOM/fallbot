
import os
from db import get_emergency_contact
from dotenv import load_dotenv
import smtplib
import sys
 
CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@messaging.sprintpcs.com"
}

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

print(EMAIL,PASSWORD)

def send_message(phone_number, carrier, message):
    print(carrier)
    print(CARRIERS[carrier])
    recipient = str(phone_number) + CARRIERS[carrier]
    auth = (EMAIL, PASSWORD)
 
    server = smtplib.SMTP('SMTP.office365.com', 587)
    server.ehlo()
    server.starttls()
    print(auth[0], auth[1])
    server.login(auth[0], auth[1])
 
    server.sendmail(auth[0], recipient, message)
 


def draft_emergency_message():
    emergency_contact = get_emergency_contact()
    print("SENDING MESSAGE TO:", emergency_contact)
