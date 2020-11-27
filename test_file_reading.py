import telebot
import json
import config
from telebot import types


class FileReader:
    client = telebot.TeleBot(config.token)

    def __init__(self, file_name):
        with open(file_name, "r") as f:
            self.question_list = json.load(f)

    @client.message_handler()
    def get_question(self, concrete_question):
        markup_inline = types.InlineKeyboardMarkup()
        text = concrete_question['question_text']
        answers = concrete_question['answers']
        list_of_answers = list()
        for answer in answers:
            list_of_answers.append(types.InlineKeyboardButton(text=str(answer["text"]),
                                                              callback_data=str(answer["is_true"])))
        markup_inline.add(list_of_answers)
        self.client.send_message(self.client.message.chat_id, str(text) +
                                 ". Выберите один правильный вариант ответа:", reply_markup=markup_inline)

    @client.callback_query_handler(func=lambda call: True)
    def count_points(call):
