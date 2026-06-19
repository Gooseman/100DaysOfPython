from quote_retriever import QuoteRetriever
from ui import QuoteUi

def get_quote():
    quote, author = QuoteRetriever().get_quote()

    if quote and author:
        print(f'"{quote}" - {author}')
    else:
        print("Failed to retrieve quote.")

if __name__ == "__main__":
    # get_quote()
    QuoteUi(QuoteRetriever().get_quote)
