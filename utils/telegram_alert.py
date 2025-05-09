import os
import sys
import asyncio
from telegram import Bot
from telegram.error import TelegramError

# Bot credentials from env or defaults
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "7933546130:AAGD1KWOV6Bvdef_AZLcRnEXV5IHARhyC48")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "1317109159")

async def send_telegram_alert(message: str):
    try:
        bot = Bot(token=TELEGRAM_BOT_TOKEN)
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
        print("Telegram alert sent successfully.")
    except TelegramError as e:
        print(f"Telegram error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        msg = " ".join(sys.argv[1:])
    else:
        msg = "Quasar default alert test."

    asyncio.run(send_telegram_message(msg))
