
def read_birthdays():
    import pandas as pd

    try:
        return pd.read_csv("data/birthdays.csv").groupby(["Month", "Day"])
    except FileNotFoundError:
        return pd.DataFrame()
    