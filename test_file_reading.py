import telebot
import json


def get_question(file_name):
    with open(file_name, "r") as f:
        question = json.load(f)


