from telebot import types


def register_start_handler(bot) -> None:
    @bot.message_handler(commands=["start"])
    def send_welcome(message: types.Message) -> None:
        bot.reply_to(
            message = message,
            text = "Привет!\nЯ ChatGPT 4o-mini Telegram Bot\U0001F916\nЗадай мне любой вопрос и я постараюсь "
                   "на него ответить",
        )