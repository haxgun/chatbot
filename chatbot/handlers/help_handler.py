from telebot import types


def register_help_handler(bot) -> None:
    @bot.message_handler(commands=["help"])
    def bot_help(message: types.Message) -> None:
        text = (
            "Команды:\n"
            "/start - Начало работы\n"
            "/help - Справка\n"
            "/info - Информация\n"
            "/donate - Поддержать проект"
        )
        bot.reply_to(message, text)
