from all_common.requester import get_request

class QuoteRetriever:
    _url = "https://www.stoic-quotes.com/api/quotes?num=1"

    def __init__(self):
        pass

    def get_quote(self):
        response = get_request(QuoteRetriever._url)
        quote = response[0]

        return quote["text"], quote["author"]
