from telebot import types
from category_test import QuestionsBlock
from client import client
import config

current_block = None


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
    client.send_message(message.from_user.id, "Выберите тему для прохождения теста:", reply_markup=markup_inline)


@client.callback_query_handler(lambda query: query.data in [config.name_of_file_1, config.name_of_file_2,
                                                            config.name_of_file_3, config.name_of_file_4,
                                                            config.name_of_file_5, config.name_of_file_6,
                                                            config.name_of_file_7, config.name_of_file_8])
def chosen_category(call):
    global current_block
    current_block = QuestionsBlock(call.from_user.id, call.data)
    current_block.start_test()


@client.callback_query_handler(lambda query: query.data in ["true", "false"])
def get_answer(call):
    global current_block
    if call.data == "true":
        client.send_message(current_block.chat_id, text="Верный ответ")
        current_block.true_counter += 1
    else:
        client.send_message(current_block.chat_id, text="Неверный ответ")

    current_block.count += 1
    if current_block.count != len(current_block.question_list):
        current_block.print_question(next(current_block.list_iterator))
    else:
        client.send_message(call.message.chat.id, text="Тест окончен. Вы набрали " + str(current_block.true_counter) +
                                                       "/" + str(len(current_block.question_list)) + " баллов.")


client.polling(none_stop=True, interval=0)
