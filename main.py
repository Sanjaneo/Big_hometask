from client import client
import config
from client_storage import ClientStorage
from menu import create_category_menu
from resources.bot_messages import TEST_SELECT_CATEGORY, BOT_INFO_MESSAGE, BOT_START_MESSAGE


@client.message_handler(commands=["start"])
def print_info(call):
    client.send_message(call.from_user.id, BOT_START_MESSAGE)


@client.message_handler(commands=["info"])
def print_info(call):
    client.send_message(call.from_user.id, BOT_INFO_MESSAGE)


@client.message_handler(commands=["start_test"])
def print_category(message):
    client.send_message(message.from_user.id, TEST_SELECT_CATEGORY, reply_markup=create_category_menu())


@client.callback_query_handler(lambda query: query.data in config.ALL_CATEGORIES.values())
def start_category_test(call):
    ClientStorage.init_client(call.from_user, call.data).start_test()


@client.callback_query_handler(lambda query: query.data in ["true", "false"])
def get_answer(call):
    ClientStorage.get_client(call.from_user).get_answer(call.data, ClientStorage)


client.polling(none_stop=True, interval=0)
