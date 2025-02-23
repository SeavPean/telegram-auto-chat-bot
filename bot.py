from telegram import Bot
import time

# Replace with your actual bot token and channel username
BOT_TOKEN = "7329473272:AAGn0_p9RWpLMjQWlTuhUvP8I1DhK0lIvYs"
CHANNEL_ID = "https://t.me/ppstore71"

bot = Bot(token=BOT_TOKEN)

def send_message():
    bot.send_message(chat_id=CHANNEL_ID, text="Hi there! Looking for something stylish? Let me help you. 😊")

# Run the bot to send a message every hour
while True:
    send_message()
    time.sleep(3600)  # Wait for 1 hour
