from chatbot.handlers.chat_handler import register_chat_handler
from chatbot.handlers.donate_handler import register_donate_handler
from chatbot.handlers.help_handler import register_help_handler
from chatbot.handlers.info_handler import register_info_handler
from chatbot.handlers.start_handler import register_start_handler


def register_handlers(bot) -> None:
    register_start_handler(bot)
    register_info_handler(bot)
    register_help_handler(bot)
    register_donate_handler(bot)
    register_chat_handler(bot)