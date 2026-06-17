import os
import smtplib

_sender_account = os.environ.get("BIRTHDAY_SENDER_ACC_ADDRESS")
_sender_email = os.environ.get("BIRTHDAY_SENDER_EMAIL")
_smtp_server = os.environ.get("BIRTHDAY_SENDER_SMTP_SERVER")
_pwd = os.environ.get("BIRTHDAY_SENDER_PASSWORD")
_port_number = 587


def start_connection():
    """Starts a connection to the SMTP server and logs in with the provided credentials."""
    connection = smtplib.SMTP(_smtp_server, _port_number)

    connection.starttls()
    connection.login(user=_sender_account, password=_pwd)
    return connection


def send_email(connection, to_email, subject, body):
    """Sends an email using the provided SMTP connection."""
    connection.sendmail(_sender_email, to_email, f"Subject: {subject}\n\n{body}")
