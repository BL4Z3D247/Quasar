# src/notifier.py

import os
from src.supabase_logger import log_to_supabase
import requests

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def notify(message: str):
    # Log to Supabase
    log_to_supabase(message)

    # Send Telegram alert
    if TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID:
        try:
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
            data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
            response = requests.post(url, data=data)
            if response.status_code != 200:
                print(f"Telegram failed: {response.text}")
        except Exception as e:
            print(f"Telegram notification error: {e}")
