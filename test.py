import logging
import telebot
import requests
import os
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Replace with your Claude API key
CLAUDE_API_KEY = os.getenv("CLOUDAI_API_KEY")

log_dir = os.path.join(os.path.dirname(__file__), "ChatGPT_Logs")
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
logging.basicConfig(
    filename=os.path.join(log_dir, "error.log"),
    level=logging.ERROR,
    format="%(levelname)s: %(asctime)s %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)

# Initialize the Anthropic client
anthropic = Anthropic(api_key=CLAUDE_API_KEY)

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(
        message, "Hello! Send me a message, and I'll ask Claude for a response."
    )


@bot.message_handler(func=lambda message: True)
def ask_claude(message):
    user_input = message.text

    try:
        completion = anthropic.completions.create(
            model="claude-3-opus-20240229",
            max_tokens_to_sample=1000,
            prompt=f"{HUMAN_PROMPT} {user_input}{AI_PROMPT}",
        )

        claude_response = completion.completion
        bot.reply_to(message, claude_response)
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        bot.reply_to(message, error_message)


bot.polling()
