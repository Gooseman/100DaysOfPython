import pandas as pd

def read_birthdays():
    """Reads birthdays from a CSV file and returns a grouped DataFrame by (Month, Day)."""
    try:
        return pd.read_csv("data/birthdays.csv").groupby(["Month", "Day"])
    except FileNotFoundError:
        return pd.DataFrame()
    