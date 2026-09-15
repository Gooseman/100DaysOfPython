from datetime import datetime

from stock_news_alert import news_reader


def test_read_news_no_result(monkeypatch):
    monkeypatch.setattr(news_reader.offset_by_days, 'offset_date', lambda off: datetime(2020, 1, 1))
    monkeypatch.setattr(news_reader, 'requester', type('R', (), {'get_request': lambda *a, **k: []}))

    assert news_reader.read_news('SomeCo') == []


def test_read_news_no_articles(monkeypatch):
    monkeypatch.setattr(news_reader.offset_by_days, 'offset_date', lambda off: datetime(2020, 1, 1))
    monkeypatch.setattr(news_reader, 'requester', type('R', (), {'get_request': lambda *a, **k: {'status': 'ok'}}))

    assert news_reader.read_news('SomeCo') == []


def test_read_news_success(monkeypatch):
    monkeypatch.setattr(news_reader.offset_by_days, 'offset_date', lambda off: datetime(2020, 1, 1))

    sample = {'articles': [
        {'title': 'A', 'description': 'a'},
        {'title': 'B', 'description': 'b'},
        {'title': 'C', 'description': 'c'},
        {'title': 'D', 'description': 'd'}
    ]}

    monkeypatch.setattr(news_reader, 'requester', type('R', (), {'get_request': lambda *a, **k: sample}))

    res = news_reader.read_news('SomeCo')

    assert isinstance(res, list)
    assert len(res) == 3
