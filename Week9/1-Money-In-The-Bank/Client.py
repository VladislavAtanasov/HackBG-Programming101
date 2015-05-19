class Client():
    def __init__(self, id, username, balance, message, email, passw):
        self.__username = username
        self.__balance = balance
        self.__id = id
        self.__message = message
        self.__email = email
        self.__passw = passw

    def get_username(self):
        return self.__username

    def get_balance(self):
        return self.__balance

    def get_id(self):
        return self.__id

    def get_message(self):
        return self.__message

    def set_balance(self, balance):
        self.__balance = balance

    def get_email(self):
        return self.__email

    def get_passw(self):
        return self.__passw

    def set_email(self, new_email):
        self.__email = new_email

    def set_message(self, new_message):
        self.__message = new_message
