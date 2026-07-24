from datetime import datetime

def epoch_to_datetime(epoch_time: int) -> datetime:
    """
    Convert epoch time to a datetime object.

    Args:
        epoch_time (int): The epoch time in seconds.

    Returns:
        datetime: A datetime object representing the given epoch time.
    """
    return datetime.fromtimestamp(epoch_time)

def to_iso_datetime(dt: datetime) -> str:
    """
    Convert a datetime object to an ISO 8601 formatted string.

    Args:
        dt (datetime): The datetime object to convert.

    Returns:
        str: An ISO 8601 formatted string representing the given datetime.
    """
    return dt.isoformat(sep=' ', timespec='seconds')
