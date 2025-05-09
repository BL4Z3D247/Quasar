import asyncio
from telegram import Bot

TELEGRAM_BOT_TOKEN = "7933546130:AAGD1KWOV6Bvdef_AZLcRnEXV5IHARhyC48"
TELEGRAM_CHAT_ID = "1317109159"

async def send_test_alert():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text="Test: Quasar alert is live and working!")

if __name__ == "__main__":
    asyncio.run(send_test_alert())
