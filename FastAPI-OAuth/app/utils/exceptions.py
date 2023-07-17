from http import HTTPStatus


class RaiseError(Exception):
    def get_message(self):
        pass


class InvalidIDError(Exception):
    def __init__(self, invalid_id: int, item_type: str):
        self.invalid_id = invalid_id
        self.item_type = item_type
        self.status = HTTPStatus.BAD_REQUEST
        super().__init__()

    def get_message(self):
        return f"No such {self.item_type} with id {self.invalid_id} exists."


class InvalidDataError(Exception):
    def __init__(self, format):
        self.format = format
        self.status = HTTPStatus.BAD_REQUEST
        super().__init__()

    def get_message(self):
        return (
            f"Invalid data, try again with appropriate format. Format - {self.format}"
        )


class InvalidCredentailsError(Exception):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.status = HTTPStatus.UNAUTHORIZED
        super().__init__()

    def get_message(self):
        return f"Invalid login details."


class ForbiddenUserError(Exception):
    def __init__(self, id, operation):
        self.id = id
        self.operation = operation
        self.status = HTTPStatus.FORBIDDEN
        super().__init__()

    def get_message(self):
        return f"Access Denied, User with id {self.id} can not perform {self.operation} operation."
