from client import client
from question_block import QuestionsBlock
from singleton import MetaSingleton


class ClientStorage(metaclass=MetaSingleton):
    client_storage = []

    @staticmethod
    def init_client(user, data) -> QuestionsBlock:
        if ClientStorage.get_client(user) is None:
            ClientStorage.client_storage.append(QuestionsBlock(client, user, data))
        return ClientStorage.get_client(user)

    @staticmethod
    def get_client(user) -> QuestionsBlock:
        return next((x for x in ClientStorage.client_storage if x.user_id == user.id), None)

    @staticmethod
    def remove_client(user):
        ClientStorage.client_storage.remove(ClientStorage.get_client(user))
