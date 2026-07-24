import os
import requests

_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

_URL = f"https://api.telegram.org/bot{_BOT_TOKEN}/sendMessage"

def send_telegram_message(message: str):
    """
    Sends a message to a specified Telegram chat using the Telegram Bot API.

    Args:
        message (str): The message to be sent to the Telegram chat.

    Returns:
        dict: The JSON response from the Telegram API if the request is successful, otherwise an empty dictionary.
    """
    payload = {"chat_id": _CHAT_ID, "text": message}
    response = requests.post(_URL, json=payload, timeout=30)

    if response.status_code == 200:
        return response.json()

    return {}
