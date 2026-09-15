from functools import reduce
import sys

from stock_news_alert.news_reader import read_news
from stock_news_alert.price_reader import read_daily_prices, read_recent_price
from stock_news_alert.telegram import send_telegram_message

STOCK = "AXON"
COMPANY_NAME = "Axon Enterprise Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
AXON: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the
coronavirus market crash.
or
AXON: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the
coronavirus market crash.
"""

def calc_percentage(start_val: float, end_val: float) -> float:
    return (end_val - start_val) / start_val * 100.0

def send_price_change(stock: str, price_data: dict):
    today_price = f"Today: Open = {price_data['today_open']}; Current = {price_data['current']}"
    today_price_change = \
        f"Today's change = {price_data['current_price_change']:.2f} ({price_data['current_percentage_change']:.2f}%)"
    two_day_price_change = price_data["yesterdays_close"] - price_data["day_before_yesterdays_close"]
    two_day_percentage_change = \
        calc_percentage(price_data["day_before_yesterdays_close"], price_data["yesterdays_close"])
    day_before = f"{price_data["day_before_yesterday"]}: Close = {price_data["day_before_yesterdays_close"]}"
    yesterday = \
        f"{price_data["yesterday"]}: Open = {price_data["yesterdays_open"]}; Close = {price_data["yesterdays_close"]}"
    change_from_day_before = f"Two day change = {two_day_price_change:.2f} ({two_day_percentage_change:.2f}%)"
    yesterday_change = price_data["yesterdays_close"] - price_data["yesterdays_open"]
    yesterday_percentage_change = calc_percentage(price_data["yesterdays_open"], price_data["yesterdays_close"])
    change_yesterday = f"Change yesterday = {yesterday_change:.2f} ({yesterday_percentage_change:.2f})"
    msg_today = f"{today_price}\n{today_price_change}"
    msg_yesterday = f"{day_before}\n{yesterday}\n{change_from_day_before}\n{change_yesterday}"
    message = f"{stock}:\n{msg_today}\n{msg_yesterday}"

    send_telegram_message(message)

def get_float(container: dict, key: str) -> float:
    value = container.get(key, 0)

    if value:
        return float(value)

    return 0

def get_price_data(ticker_name: str):
    open_close_prices = read_daily_prices(ticker_name)
    recent_price = read_recent_price(ticker_name)

    if open_close_prices is None or len(open_close_prices) < 2:
        print("Failed to retrieve at least two daily prices for", STOCK)

    if recent_price is None or len(recent_price) == 0:
        print("Failed to retrieve recent price for", STOCK)

    current_price = get_float(recent_price, "c")
    today_open = get_float(recent_price, "o")
    yesterdays_open = get_float(open_close_prices[0][1], "1. open")
    yesterdays_close = get_float(open_close_prices[0][1], "4. close")
    day_before_yesterdays_open = get_float(open_close_prices[1][1], "1. open")
    day_before_yesterdays_close = get_float(open_close_prices[1][1], "4. close")

    if current_price == 0 \
            or today_open == 0 \
            or yesterdays_open == 0 \
            or yesterdays_close == 0 \
            or day_before_yesterdays_open == 0 \
            or day_before_yesterdays_close == 0:
        return
    
    current_price_change = current_price - today_open
    current_percentage_change = calc_percentage(today_open, current_price)
    closing_percentage_change = (
        (yesterdays_close - day_before_yesterdays_close) / yesterdays_close * 100.0
    )
    the_price_data = {
        "current": current_price,
        "today_open": today_open,
        "current_price_change": current_price_change,
        "current_percentage_change": current_percentage_change,
        "yesterday": open_close_prices[0][0] or 0,
        "yesterdays_open": yesterdays_open,
        "yesterdays_close": yesterdays_close,
        "day_before_yesterday": open_close_prices[1][0] or 0,
        "day_before_yesterdays_open": day_before_yesterdays_open,
        "day_before_yesterdays_close": day_before_yesterdays_close,
    }

    send_price_change(ticker_name, the_price_data)

    return max(abs(closing_percentage_change), abs(current_percentage_change))

def get_news(company_name: str):
    return read_news(company_name)

def send_news(company_name: str, news: list):
    articles = news[:3]

    if len(articles) == 0:
        return

    message = reduce(
        lambda msg, article: msg + f"Headline: {article['title']}\nBrief: {article['description']}\n\n",
        articles,
        "")

    send_telegram_message(f"News for {company_name}:\n{message}")

if __name__ == "__main__":
    percentage_change = get_price_data(STOCK)

    if (percentage_change < -1 or percentage_change > 1):
        print("Significant change in stock price (> 1%) for", STOCK)
        the_news = get_news(COMPANY_NAME)
        send_news(COMPANY_NAME, the_news)
