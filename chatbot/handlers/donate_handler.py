from telebot import types


def register_donate_handler(bot) -> None:
    @bot.message_handler(commands=["donate"])
    def bot_donate(message: types.Message) -> None:
        bot.reply_to(
            message = message,
            text = "Спасибо, что хотите помочь проекту развиваться! "
            "Для доната напишите: https://t.me/dan4eg"
        )
