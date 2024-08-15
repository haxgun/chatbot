from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from Bot.keyboards.inline.inline_keyboard import get_inline_keyboard_markup


class NewDialog:
    def __init__(self, message):
        self.message = message

    def handle(self) -> tuple[str, InlineKeyboardMarkup | None]:
        text = "Список ваших диалогов:"
        keyboard = self.dialog_keyboard()
        return text, keyboard

    def dialog_keyboard(self) -> InlineKeyboardMarkup:
        buttons = [
            InlineKeyboardButton(text='Dialog 1', callback_data='dialog_1'),
            InlineKeyboardButton(text='Dialog 2', callback_data='dialog_2'),
            InlineKeyboardButton(text='Dialog 3', callback_data='dialog_3'),
            InlineKeyboardButton(text='Dialog 4', callback_data='dialog_4'),
        ]
        return get_inline_keyboard_markup(buttons)
