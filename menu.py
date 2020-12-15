from telebot import types

import config


def create_category_menu():
    markup_inline = types.InlineKeyboardMarkup()
    for key, value in config.ALL_CATEGORIES.items():
        markup_inline.add(types.InlineKeyboardButton(text=key, callback_data=value))
    return markup_inline
