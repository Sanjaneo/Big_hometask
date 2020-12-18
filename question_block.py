import os
import json
from telebot import types
from resources.bot_messages import QUESTION, TEST_PASS_ANSWER, TEST_FAIL_ANSWER, TEST_RESULT_MESSAGE


class QuestionsBlock:
    def __init__(self, client, user, file_name):
        self.client = client
        self.user = user
        self.user_id = self.user.id

        with open(f'{os.getcwd()}/resources/questions/{file_name}.json', mode="r", encoding="utf8") as f:
            self.question_list: dict = json.load(f)
        self.count = 0
        self.true_counter = 0
        self.list_iterator = iter(self.question_list.values())

    def start_test(self):
        self.print_question(next(self.list_iterator))

    def print_question(self, concrete_question):
        markup_inline = types.InlineKeyboardMarkup()
        text = concrete_question['question_text']
        answers = concrete_question['answers']
        for k, value in answers.items():
            markup_inline.add(types.InlineKeyboardButton(text=str(value["text"]),
                                                         callback_data=str(value["is_true"])))

        self.client.send_message(chat_id=self.user_id,
                                 text=QUESTION.format(text=text),
                                 reply_markup=markup_inline)

    def get_answer(self, data, client_storage):
        if data == "true":
            self.client.send_message(chat_id=self.user_id, text=TEST_PASS_ANSWER)
            self.true_counter += 1
        else:
            self.client.send_message(chat_id=self.user_id, text=TEST_FAIL_ANSWER)

        self.count += 1
        if self.count != len(self.question_list):
            self.print_question(next(self.list_iterator))
        else:
            self.client.send_message(chat_id=self.user_id,
                                     text=TEST_RESULT_MESSAGE.format(res_count=self.true_counter,
                                                                     total_count=len(self.question_list)))
            client_storage.remove_client(self.user)
