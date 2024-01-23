import telebot
import openai


from .env import API_KEY, YOUR_TOKEN

openai.api_key = {API_KEY}
TOKEN = {YOUR_TOKEN}
bot = telebot.TeleBot(TOKEN)

# Добавьте глобальный словарь для хранения истории переписки
chat_histories = {}

@bot.message_handler(func=lambda _: True)
def handle_message(message):
    chat_id = message.chat.id

    # Проверьте, есть ли история переписки для данного пользователя
    if chat_id not in chat_histories:
        chat_histories[chat_id] = [
            {"role": "system", "content": "You are a helpful assistant."},
        ]

    chat_histories[chat_id].append({"role": "user", "content": message.text})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_histories[chat_id],
        max_tokens=1000,
        temperature=0.5,
        n=1,
        stop=None,
        timeout=None,
        presence_penalty=0.0,
        frequency_penalty=0.5,
    )

    # Добавьте ответ ассистента в историю переписки
    chat_histories[chat_id].append({"role": "assistant", "content": response['choices'][0]['message']['content'].strip()})

    bot.send_message(chat_id=chat_id, text=response['choices'][0]['message']['content'].strip())

bot.polling()
