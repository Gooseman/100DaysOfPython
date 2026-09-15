from stock_news_alert import main


def test_calc_percentage():
    assert main.calc_percentage(100, 110) == 10.0
    assert main.calc_percentage(50, 25) == -50.0


def test_get_float():
    assert main.get_float({'a': '2.5'}, 'a') == 2.5
    assert main.get_float({}, 'missing') == 0
    assert main.get_float({'x': 0}, 'x') == 0


def test_send_price_change_calls_telegram(monkeypatch):
    sent = {}

    def fake_send(msg):
        sent['msg'] = msg

    monkeypatch.setattr(main, 'send_telegram_message', fake_send)

    price_data = {
        'current': 105,
        'today_open': 100,
        'current_price_change': 5,
        'current_percentage_change': 5.0,
        'yesterday': '2021-01-02',
        'yesterdays_open': 98,
        'yesterdays_close': 102,
        'day_before_yesterday': '2021-01-01',
        'day_before_yesterdays_open': 95,
        'day_before_yesterdays_close': 97,
    }

    main.send_price_change('TST', price_data)
    assert 'msg' in sent
    assert 'TST' in sent['msg']


def test_send_news(monkeypatch):
    sent = {}

    def fake_send(msg):
        sent['msg'] = msg

    monkeypatch.setattr(main, 'send_telegram_message', fake_send)

    # empty news -> no send
    main.send_news('Co', [])
    assert not sent

    articles = [
        {'title': 'One', 'description': 'one'},
        {'title': 'Two', 'description': 'two'}
    ]
    main.send_news('Co', articles)
    assert 'msg' in sent and 'Headline:' in sent['msg']
