import requests
from django.conf import settings
import os
from dotenv import load_dotenv

load_dotenv()


def telegram_messages(text: str) -> bool:
    token =  os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        raise RuntimeError("Telegram bot token or chat id is not configured.")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    response = requests.post(url, json=payload, timeout=10)
    response.raise_for_status()

    result = response.json()
    return result.get("ok", False)