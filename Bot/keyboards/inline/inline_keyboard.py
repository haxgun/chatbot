from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_inline_keyboard_markup(buttons: list[InlineKeyboardButton] = None) -> InlineKeyboardMarkup:
    initial_keyboard = InlineKeyboardMarkup(row_width=2)
    if buttons:
        for button in buttons:
            initial_keyboard.add(button)
    return initial_keyboard
