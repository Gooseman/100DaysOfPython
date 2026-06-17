from birthdays_reader import read_birthdays
from dates import get_today
from emailer import send_email, start_connection

def get_all_birthdays():
    """Reads all birthdays from the CSV file and returns a dictionary of birthdays grouped by (month, day)."""
    raw_birthdays = read_birthdays()
    birthdays_by_date = {
        date: group.to_dict(orient="records") for date, group in raw_birthdays
    }

    return birthdays_by_date


def get_todays_birthdays(birthdays):
    """Returns a list of birthdays for today."""
    today = get_today()
    return birthdays.get((today[1], today[2]), [])


def send_birthday_wishes(birthdays):
    """Sends birthday wishes to all users whose birthday is today."""
    with start_connection() as connection:
        for person in birthdays:
            print(f"Sending for birthday: {person}")
            send_birthday_wish(connection, person)


def send_birthday_wish(connection, person):
    """Sends a birthday wish to a single user."""
    age = get_age(person["Year"])

    send_email(
        connection,
        person["Email"],
        "Happy Birthday!",
        f"Happy {age} birthday, {person['Name']}! I hope you have a great day!",
    )


def get_age(birth_year):
    """Returns the age of a person given their birth year with an appropriate suffix (st, nd, rd, th)."""
    current_year = get_today()[0]
    age = str(current_year - birth_year)

    if age.endswith("1") and not age.endswith("11"):
        return f"{age}st"
    elif age.endswith("2") and not age.endswith("12"):
        return f"{age}nd"
    elif age.endswith("3") and not age.endswith("13"):
        return f"{age}rd"
    else:
        return f"{age}th"
