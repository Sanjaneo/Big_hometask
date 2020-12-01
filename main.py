from time import sleep

from telebot import types
from client import client, chat_id
import config

from file_reading import FileReader


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
    client.send_message(chat_id, "Выберите тему для прохождения теста:", reply_markup=markup_inline)


@client.callback_query_handler(lambda query: query.data in [config.name_of_file_1, config.name_of_file_2])
def chosen_category(call):
    file_reader = FileReader(call.data)

    for key, value in file_reader.question_list.items():
        file_reader.get_question(chat_id, value)

    client.send_message(call.message.chat.id, text="Тест окончен. Вы набрали " + str(file_reader.count) +
                                                   "/" + str(len(file_reader.question_list)) + " баллов.")


@client.callback_query_handler(lambda query: query.data in ["true", "false"])
def get_answer(call):
    if call.data == "true":
        client.send_message(chat_id, text="Верный ответ")
    else:
        client.send_message(chat_id, text="Неверный ответ")


def get_question(concrete_question):
    markup_inline = types.InlineKeyboardMarkup()
    text = concrete_question['question_text']
    answers = concrete_question['answers']
    list_of_answers = list()
    for k, value in answers.items():
        list_of_answers.append(types.InlineKeyboardButton(text=str(value["text"]),
                                                          callback_data=str(value["is_true"])))
        markup_inline.add(list_of_answers)
    client.send_message(chat_id,
                        text=f"{text}. Выберите один правильный вариант ответа:",
                        reply_markup=markup_inline)


client.polling(none_stop=True, interval=0)
