import openai
import telebot

from Bot.config_data.config import logger
from Bot.handlers.default_handlers.start import *  # noqa # pylint: disable=unused-import
from Bot.handlers.service_handlers.navigation import *  # noqa # pylint: disable=unused-import


@bot.message_handler(func=lambda _: True)
def handle_message(message: Message):
    prompt = message.text
    response = generate_response(prompt)
    bot.send_message(chat_id=message.from_user.id, text=response)


def generate_response(prompt):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    return completion.choices[0].message.content


if __name__ == '__main__':
    logger.info("ChatGPT Bot is working")

    try:
        bot.infinity_polling(restart_on_change=True)
    except (telebot.apihelper.ApiException, ConnectionError) as e:
        logger.exception(e)
