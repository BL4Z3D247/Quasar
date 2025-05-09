import asyncio
import telegram

# Define the Bot token and Chat ID
TELEGRAM_BOT_TOKEN = "7933546130:AAGD1KWOV6Bvdef_AZLcRnEXV5IHARhyC48"
TELEGRAM_CHAT_ID = "1317109159"  # Same as previously stated

# Initialize the Telegram bot with the provided token
bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

# Asynchronous function to send a test message
async def send_test_message():
    try:
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text="Test: Quasar Bot is live!")
        print("Test message sent successfully.")
    except Exception as e:
        print(f"Error sending message: {str(e)}")

# Run the function in the event loop
if __name__ == "__main__":
    asyncio.run(send_test_message())
