from client import client
from question_block import QuestionsBlock
from singleton import MetaSingleton


class ClientStorage(metaclass=MetaSingleton):
    client_storage = []

    @staticmethod
    def init_client(chat_id, data) -> QuestionsBlock:
        if ClientStorage.get_client(chat_id) is None:
            ClientStorage.client_storage.append(QuestionsBlock(client, chat_id, data))
        return ClientStorage.get_client(chat_id)

    @staticmethod
    def get_client(chat_id) -> QuestionsBlock:
        return next((x for x in ClientStorage.client_storage if x.chat_id == chat_id), None)

    @staticmethod
    def remove_client(chat_id):
        ClientStorage.client_storage.remove(ClientStorage.get_client(chat_id))
