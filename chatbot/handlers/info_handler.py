from telebot import types


def register_info_handler(bot) -> None:
    @bot.message_handler(commands=["info"])
    def bot_info(message: types.Message) -> None:
        bot.reply_to(
            message = message,
            text = "Используется ChatGPT 4o-mini, но почему-то он говорит, что он 3.5... Длина контекста 4096 символов."
        )
