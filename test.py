import logging
import telebot
import requests
import os

from dotenv import load_dotenv


load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Replace with your Claude API key
CLAUDE_API_KEY = os.getenv("CLOUDAI_API_KEY")

# Claude API endpoint
CLAUDE_API_URL = "https://api.anthropic.com/v1/chat/completions"

log_dir = os.path.join(os.path.dirname(__file__), "ChatGPT_Logs")
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
logging.basicConfig(
    filename=os.path.join(log_dir, "error.log"),
    level=logging.ERROR,
    format="%(levelname)s: %(asctime)s %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(
        message, "Hello! Send me a message, and I'll ask Claude for a response."
    )


@bot.message_handler(func=lambda message: True)
def ask_claude(message):
    user_input = message.text

    headers = {
        "Content-Type": "application/json",
        "x-api-key": CLAUDE_API_KEY,
        "anthropic-version": "2023-06-01",
    }

    data = {
        "model": "claude-3-opus-20240229",
        "max_tokens": 1000,
        "messages": [{"role": "user", "content": user_input}],
    }

    try:
        response = requests.post(CLAUDE_API_URL, json=data, headers=headers)
        response.raise_for_status()

        claude_response = response.json()["choices"][0]["message"]["content"]
        bot.reply_to(message, claude_response)
    except requests.exceptions.RequestException as e:
        bot.reply_to(message, f"An error occurred: {str(e)}")


bot.polling()
