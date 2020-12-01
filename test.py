import telebot
import config
from telebot import types
from file_reading import FileReader
from result import Result

client = telebot.TeleBot(config.token)


@client.message_handler(commands=["start_test"])
def get_category(message):
    markup_inline = types.InlineKeyboardMarkup()
    category_1 = types.InlineKeyboardButton(text=config.seminar_1, callback_data=config.name_of_file_1)
    category_2 = types.InlineKeyboardButton(text=config.seminar_2, callback_data=config.name_of_file_2)
    category_3 = types.InlineKeyboardButton(text=config.seminar_3, callback_data=config.name_of_file_3)
    category_4 = types.InlineKeyboardButton(text=config.seminar_4, callback_data=config.name_of_file_4)
    category_5 = types.InlineKeyboardButton(text=config.seminar_5, callback_data=config.name_of_file_5)
    category_6 = types.InlineKeyboardButton(text=config.seminar_6, callback_data=config.name_of_file_6)
    category_7 = types.InlineKeyboardButton(text=config.seminar_7, callback_data=config.name_of_file_7)
    category_8 = types.InlineKeyboardButton(text=config.seminar_8, callback_data=config.name_of_file_8)

    markup_inline.add(category_1, category_2, category_3, category_4, category_5, category_6, category_7, category_8)
    client.send_message(message.chat_id, "Выберите тему для прохождения теста:", reply_markup=markup_inline)


@client.callback_query_handler(func=lambda call: True)
def chosen_category(call):
    file_reader = FileReader(call.data)

    for concrete_question in file_reader.question_list:
        file_reader.get_question(concrete_question)
        file_reader.count_points()

    client.send_message(id, text=)