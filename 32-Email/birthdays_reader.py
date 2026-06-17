
def read_birthdays():
    """Reads birthdays from a CSV file and returns a grouped DataFrame by (Month, Day)."""
    import pandas as pd

    try:
        return pd.read_csv("data/birthdays.csv").groupby(["Month", "Day"])
    except FileNotFoundError:
        return pd.DataFrame()
    