import openai

from telebot import types

from chatbot.dialog_manager import save_dialog, load_dialog_context


def register_chat_handler(bot) -> None:
    @bot.message_handler(func=lambda _: True)
    def handle_message(message: types.Message) -> None:
        user_id = message.from_user.id
        prompt = message.text

        dialog_id = 'current_dialog_id'
        context = load_dialog_context(user_id, dialog_id)

        messages = [{"role": "user", "content": msg['prompt']} for msg in context]
        messages.append({"role": "user", "content": prompt})

        completion = openai.ChatCompletion.create(model="gpt-4o-mini", messages=messages)
        response = completion.choices[0].message.content

        save_dialog(user_id, dialog_id, prompt, response)

        bot.send_message(chat_id=user_id, text=response)