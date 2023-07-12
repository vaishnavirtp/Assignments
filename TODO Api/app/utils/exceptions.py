from abc import abstractmethod, ABC


class RaiseError(Exception, ABC):
    def get_message_for_dev(self):
        pass

    def get_message_for_client(self):
        pass


class InvalidIDError(Exception, ABC):
    def __init__(self, invalid_id: int, item_type: str):
        self.invalid_song_id = invalid_id
        self.item_type = item_type
        super().__init__()

    def get_message_for_dev(self):
        return f"Invalid song id -{self.invalid_song_id}"

    def get_message_for_client(self):
        print(self.item_type)
        return f"No such {self.item_type} exists."


class InvalidDataError(Exception, ABC):
    def __init__(self):
        super().__init__()

    def get_message_for_dev(self):
        return f"Invalid Data posted."

    def get_message_for_client(self):
        print(self.item_type)
        return f"Invalid data, try again with appropriate format."
