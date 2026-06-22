import requests

class QuoteRetriever:
    _url = "https://www.stoic-quotes.com/api/quotes?num=1"

    def __init__(self):
        pass

    def get_quote(self):
        try:
            response = requests.get(QuoteRetriever._url, timeout=15)

            response.raise_for_status()

            quote = response.json()[0]

            return quote["text"], quote["author"]
        except requests.ConnectTimeout:
            print("Connection to the quote API timed out.")
            return None, None
        except requests.ConnectionError:
            print("Failed to connect to the quote API.")
            return None, None
        except requests.Timeout:
            print("The request to the quote API timed out.")
            return None, None
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None, None
        except requests.RequestException as e:
            print(f"Error retrieving quote: {e}")
            return None, None
