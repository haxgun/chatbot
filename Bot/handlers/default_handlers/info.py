from telebot.types import Message

from config_data.config import DEFAULT_COMMANDS
from loader import bot


@bot.message_handler(commands=["info"])
def bot_info(message: Message):
    bot.reply_to(message, f"Данный бот предназначен для чего то большего")
