import datetime as dt

def get_today():
    now = dt.datetime.now()

    return (now.year, now.month, now.day)
