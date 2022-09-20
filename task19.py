from string import digits
from string import ascii_uppercase
from string import ascii_letters


class Registration:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login):
        if login.count('@') >= 1:
            if login.count('.') >= 1:
                self.__login = login
            else:
                print('Має бути мінімум одна крапка')
        else:
            print('має бути мінімум один символ "@"')

    @staticmethod
    def is_include_digit(value):
        for digit in value:
            if digit in digits:
                return True
        return False

    @staticmethod
    def is_include_all_register(value):
        k = 0
        for v in value:
            if v in ascii_uppercase:
                k += 1
        if k >= 2:
            return True
        else:
            return False

    @staticmethod
    def is_include_only_latin(value):
        for i in value:
            if i not in ascii_letters + digits:
                return False
        return True

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if not isinstance(password, str):
            raise TypeError('Пароль має бути рядком')
        if not 4 <= len(password) <= 12:
            raise ValueError('Пароль має бути не манше 4 символів і не більше 12')
        if not Registration.is_include_digit(password):
            raise ValueError(f'Пароль повинен містити хочаб одну цифру')
        if not Registration.is_include_all_register(password):
            raise ValueError(f'Пароль має містити хочаб 2 великі літери')
        if not Registration.is_include_only_latin(password):
            raise ValueError('Пароль повинен містити лише латинські букви')
        self.__password = password


q = Registration('asd@.', 'hjLKl8l')
print(q.login, q.password)