import os

from all_common import requester

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")
TIME_SERIES_DAILY_KEY = "Time Series (Daily)"

def read_daily_prices(ticker_name: str):
    result = requester.get_request(
        "https://www.alphavantage.co/query",
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": ticker_name,
            "apikey": ALPHAVANTAGE_API_KEY
        }
    )

    if result == {}:
        print("Failed to retrieve data for", ticker_name)
        return None

    if TIME_SERIES_DAILY_KEY not in result:
        print("Time series data not found for", ticker_name)
        print(result)
        return None

    return list(result[TIME_SERIES_DAILY_KEY].items())[:2]

def read_recent_price(ticker_name: str):
    result = requester.get_request(
        "https://finnhub.io/api/v1/quote",
        params = {
            "symbol": ticker_name,
            "token": FINNHUB_API_KEY
        }
    )

    print(result)
    return result
