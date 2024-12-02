import openai
from telebot.types import Message

from config import bot
from dialog_manager import save_dialog, load_dialog_context


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(
        message,
        "Привет!\nЯ ChatGPT 4o-mini Telegram Bot\U0001F916\nЗадай мне любой вопрос и я постараюсь на него ответить",
    )


@bot.message_handler(commands=["info"])
def bot_info(message: Message):
    bot.reply_to(
        message, "Используется ChatGPT 4o-mini, но почему то он говорит что он 3.5... Длинна контекста 4096 символов."
    )


@bot.message_handler(commands=["help"])
def bot_help(message: Message):
    text = (
        "Команды:\n" "/start - Начало работы\n" "/help - Справка\n" "/info - Информация\n" "/donate - Поддержать проект"
    )
    bot.reply_to(message, text)


@bot.message_handler(commands=["donate"])
def bot_info(message: Message):
    bot.reply_to(message, "Спасибо что хотите помочь проекту развиваться!." "Для доната напишите https://t.me/dan4eg")


@bot.message_handler(func=lambda _: True)
def handle_message(message: Message):
    user_id = message.from_user.id
    prompt = message.text

    # Загрузить текущий диалог
    dialog_id = 'current_dialog_id'  # Используйте механизм генерации ID диалога
    context = load_dialog_context(user_id, dialog_id)

    # Формирование сообщений с контекстом
    messages = [{"role": "user", "content": msg['prompt']} for msg in context]
    messages.append({"role": "user", "content": prompt})

    # Запрос к OpenAI
    completion = openai.ChatCompletion.create(model="gpt-4o-mini", messages=messages)
    response = completion.choices[0].message.content

    # Сохранение диалога
    save_dialog(user_id, dialog_id, prompt, response)

    # Отправка ответа пользователю
    bot.send_message(chat_id=user_id, text=response)


if __name__ == '__main__':
    bot.infinity_polling()
