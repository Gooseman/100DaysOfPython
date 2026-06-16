import smtplib

_sender_account = "craigbarrett.za@gmail.com"
_sender_email = "fake@duck.com"
_pwd = "yvsb gwap egrk dseh"
_port_number = 587


def start_connection():
    connection = smtplib.SMTP("smtp.gmail.com", _port_number)

    connection.starttls()
    connection.login(user=_sender_account, password=_pwd)
    return connection


def send_email(connection, to_email, subject, body):
    connection.sendmail(_sender_email, to_email, f"Subject: {subject}\n\n{body}")
    # connection.sendmail(from_addr="fake@gmail.com", to_addrs=[to_email], msg=body)
