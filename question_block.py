import json
from telebot import types


class QuestionsBlock:
    def __init__(self, client, chat_id, file_name):
        with open(file_name, "r") as f:
            self.question_list: dict = json.load(f)
        self.client = client
        self.count = 0
        self.chat_id = chat_id
        self.true_counter = 0
        self.list_iterator = iter(self.question_list.values())

    def start_test(self):
        self.print_question(next(self.list_iterator))

    def print_question(self, concrete_question):
        markup_inline = types.InlineKeyboardMarkup()
        text = concrete_question['question_text']
        answers = concrete_question['answers']
        for k, value in answers.items():
            markup_inline.add(types.InlineKeyboardButton(text=str(value["text"]), callback_data=str(value["is_true"])))

        self.client.send_message(self.chat_id,
                                 text=f"{text}. Выберите один правильный вариант ответа:",
                                 reply_markup=markup_inline)
