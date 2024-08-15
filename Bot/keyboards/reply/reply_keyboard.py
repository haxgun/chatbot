from telebot.types import KeyboardButton, ReplyKeyboardMarkup


def get_reply_keyboard_markup(buttons: list[KeyboardButton] = None) -> ReplyKeyboardMarkup:
    initial_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    if buttons:
        for button in buttons:
            initial_keyboard.add(button)
    return initial_keyboard


def get_initial_keyboard(buttons: list[KeyboardButton] = None) -> ReplyKeyboardMarkup:
    if buttons is None:
        buttons = []

    buttons.extend(
        [
            KeyboardButton('Выбрать диалог'),
            KeyboardButton('Новый диалог'),
            KeyboardButton('Донат'),
        ]
    )

    return get_reply_keyboard_markup(buttons)
