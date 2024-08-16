from dotenv import load_dotenv
import smtplib
import ssl
import os

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

host = "smtp.office365.com"
port = 587
context = ssl.create_default_context()
message = "Hello World!"

with smtplib.SMTP(host, port) as server:
    server.ehlo(host)
    server.starttls(context=context)
    server.ehlo(host)

    server.login(EMAIL, PASSWORD)
    server.sendmail(EMAIL, "example@gmail.com", message)
