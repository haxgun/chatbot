from telebot import TeleBot, StateMemoryStorage

from chatbot.config import BOT_TOKEN
from chatbot.handlers import register_handlers


class TelegramBot(TeleBot):
    def __init__(self):
        super().__init__(BOT_TOKEN, state_storage=StateMemoryStorage())

        register_handlers(self)

    def run(self) -> None:
        self.infinity_polling()
