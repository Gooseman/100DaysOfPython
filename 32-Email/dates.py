import datetime as dt

def get_today():
    """Returns the current date as a tuple (year, month, day)."""
    now = dt.datetime.now()

    return (now.year, now.month, now.day)
