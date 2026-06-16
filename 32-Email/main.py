from birthday_wisher import get_all_birthdays, get_todays_birthdays, send_birthday_wishes
from dates import get_today

def send_test_email():
    # with start_connection() as connection:
    #     send_email(
    #         connection, 
    #         f"fake_at_protonmail.com_{_sender_email}", 
    #         # "fake@protonmail.com", 
    #         "Test Email", 
    #         "This is a test email sent from Python.")
    pass

def wish_happy_birthday():
    birthdays = get_all_birthdays()
    # print(birthdays)
    todays_birthdays = get_todays_birthdays(birthdays)

    if todays_birthdays:
        send_birthday_wishes(todays_birthdays)


if __name__ == "__main__":
    send_test_email()

    current_day = get_today()
    today = (current_day[1], current_day[2])
    # print(today)

    wish_happy_birthday()
