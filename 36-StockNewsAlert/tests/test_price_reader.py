
from stock_news_alert import price_reader


def test_read_daily_prices_empty(monkeypatch):
    monkeypatch.setattr(price_reader.requester, 'get_request', lambda url, params=None: {})

    assert price_reader.read_daily_prices('ABC') is None


def test_read_daily_prices_no_key(monkeypatch):
    monkeypatch.setattr(price_reader.requester, 'get_request', lambda url, params=None: {'Meta Data': {}})

    assert price_reader.read_daily_prices('ABC') is None


def test_read_daily_prices_success(monkeypatch):
    data = {"Time Series (Daily)": {
        "2021-01-02": {"1. open": "10", "4. close": "12"},
        "2021-01-01": {"1. open": "9", "4. close": "11"}
    }}

    monkeypatch.setattr(price_reader.requester, 'get_request', lambda url, params=None: data)

    res = price_reader.read_daily_prices('ABC')

    assert isinstance(res, list)
    assert len(res) == 2


def test_read_recent_price_returns_dict(monkeypatch):
    sample = {"c": 100, "o": 95}

    monkeypatch.setattr(price_reader.requester, 'get_request', lambda url, params=None: sample)
    assert price_reader.read_recent_price('ABC') == sample
