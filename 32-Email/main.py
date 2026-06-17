from birthday_wisher import get_all_birthdays, get_todays_birthdays, send_birthday_wishes
from dates import get_today

def wish_happy_birthday():
    """Wishes happy birthday to all users whose birthday is today."""
    birthdays = get_all_birthdays()
    todays_birthdays = get_todays_birthdays(birthdays)

    print(f"Today's birthdays: {todays_birthdays}")

    if todays_birthdays:
        send_birthday_wishes(todays_birthdays)


if __name__ == "__main__":
    current_day = get_today()
    today = (current_day[1], current_day[2])

    wish_happy_birthday()
