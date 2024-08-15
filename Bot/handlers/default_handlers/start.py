from telebot.types import Message

from Bot.config_data.config import bot
from Bot.keyboards.reply.reply_keyboard import get_initial_keyboard


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(
        message,
        "Привет!\nЯ ChatGPT 3.5 Telegram Bot\U0001F916\nЗадай мне любой вопрос и я постараюсь на него ответить",
        reply_markup=get_initial_keyboard(),
    )
