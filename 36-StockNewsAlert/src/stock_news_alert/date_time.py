from datetime import datetime, timedelta, timezone

def from_est_to_utc(est_datetime):
    # EST is UTC-5
    est_offset = timedelta(hours=-5)
    est_datetime = est_datetime.replace(tzinfo=timezone(est_offset))

    return est_datetime.astimezone(timezone.utc)

def offset_date(offset_days: int):
    return datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=offset_days)
