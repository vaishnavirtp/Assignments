from http import HTTPStatus


class InvalidIDError(Exception):
    def __init__(self, invalid_id: int, item_type: str):
        self.invalid_song_id = invalid_id
        self.item_type = item_type
        self.status = HTTPStatus.UNAUTHORIZED
        super().__init__()

    def __str__(self) -> str:
        return f"Invalid song id -{self.invalid_song_id}"


class InvalidDataError(Exception):
    def __init__(self):
        super().__init__()
        self.status = HTTPStatus.BAD_REQUEST

    def __str__(self) -> str:
        return f"Invalid Data posted."
