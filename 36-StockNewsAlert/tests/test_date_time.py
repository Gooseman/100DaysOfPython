from datetime import datetime, timezone, timedelta

from stock_news_alert import date_time


def test_from_est_to_utc():
    hour = 12
    est = datetime(2020, 1, 1, hour, 0, 0)
    utc = date_time.from_est_to_utc(est)

    assert utc.tzinfo == timezone.utc
    # EST is UTC-5, so 12:00 EST -> 17:00 UTC
    assert utc.hour == hour + 5

def test_offset_date_zero():
    od = date_time.offset_date(0)

    assert od.hour == 0 and od.minute == 0 and od.second == 0 and od.microsecond == 0


def test_offset_date_nonzero():
    offset = 1
    od = date_time.offset_date(offset)

    assert (datetime.now() + timedelta(days=offset)).date() == od.date()
