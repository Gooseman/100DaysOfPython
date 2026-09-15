
import os

import stock_news_alert.date_time as offset_by_days
from stock_news_alert import requester

NEWSORG_API_KEY = os.getenv("NEWSORG_API_KEY")

def read_news(company_name: str):
    result = requester.get_request(
        "https://newsapi.org/v2/everything",
        params = {
            "q": company_name,
            "from": offset_by_days.offset_date(-3).isoformat(),
            "apiKey": NEWSORG_API_KEY,
            "sortBy": "relevancy"
        }
    )

    if len(result) == 0:
        print("No news retrieved for", company_name)
        return []

    if "articles" not in result:
        print("No articles found for", company_name)
        return []

    return result["articles"][:3]
