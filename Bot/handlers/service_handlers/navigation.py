from Bot.config_data.config import bot
from Bot.handlers.service_handlers.dialog import NewDialog


@bot.message_handler(func=lambda message: message.text == 'Выбрать диалог')
def new_dialog(message):
    dialog = NewDialog(message)
    text, new_kb = dialog.handle()
    bot.reply_to(message, text, reply_markup=new_kb)
