from dataobjects.default_data_object import DefaultDataObject


class SignInData(DefaultDataObject):
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
