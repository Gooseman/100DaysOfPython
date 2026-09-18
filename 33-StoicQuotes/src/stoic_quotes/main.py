from stoic_quotes.quote_retriever import QuoteRetriever
from stoic_quotes.quote_ui import QuoteUi
from stoic_quotes.telegram import send_telegram_message

def send_quote():
    quote, author = QuoteRetriever().get_quote()

    if quote and author:
        print(f'"{quote}" - {author}')
        send_telegram_message(f'"{quote}" - {author}')
    else:
        print("Failed to retrieve quote.")

if __name__ == "__main__":
    # QuoteUi(QuoteRetriever().get_quote)
    send_quote()
