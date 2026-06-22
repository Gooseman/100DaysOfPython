import os
import smtplib

SESNDER_ACCOUNT = os.environ.get("BIRTHDAY_SENDER_ACC_ADDRESS")
SENDER_EMAIL = os.environ.get("BIRTHDAY_SENDER_EMAIL")
SMTP_SERVER = os.environ.get("BIRTHDAY_SENDER_SMTP_SERVER")
PWD = os.environ.get("BIRTHDAY_SENDER_PASSWORD")
PORT_NUMBER = 587


def start_connection():
    """Starts a connection to the SMTP server and logs in with the provided credentials."""
    connection = smtplib.SMTP(SMTP_SERVER, PORT_NUMBER)

    connection.starttls()
    connection.login(user=SESNDER_ACCOUNT, password=PWD)
    return connection


def send_email(connection, to_email, subject, body):
    """Sends an email using the provided SMTP connection."""
    connection.sendmail(SENDER_EMAIL, to_email, f"Subject: {subject}\n\n{body}")
