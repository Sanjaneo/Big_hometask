import json
from telebot import types
from client import client


class FileReader:
    def __init__(self, file_name):
        with open(file_name, "r") as f:
            self.question_list = json.load(f)
        self.count = 0

    # @client.message_handler()
    def get_question(self, chat_id, concrete_question):
        markup_inline = types.InlineKeyboardMarkup()
        text = concrete_question['question_text']
        answers = concrete_question['answers']
        for k, value in answers.items():
            markup_inline.add(types.InlineKeyboardButton(text=str(value["text"]),
                                                         callback_data=str(value["is_true"])))

        client.send_message(chat_id,
                            text=f"{text}. Выберите один правильный вариант ответа:",
                            reply_markup=markup_inline)

    # @client.callback_query_handler(func=lambda call: True)
    # def count_points(self, call):
    #     if call.data == "true":
    #         self.count += 1
