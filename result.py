import telebot
import config
from file_reading import FileReader

class Result:
    client = telebot.TeleBot(config.token)

    @client.send_message()
    def send_result(count):
