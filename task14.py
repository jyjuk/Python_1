class UserMail:

    def __init__(self, login, email):
        self.login = login
        self.email = email

    def get_email(self):
        return self.__email

    def set_email(self, values):
        if isinstance(values, str)\
                and values.count('@') == 1 \
                and '.' in values[values.find('@'):]:
            self.__email = values
        else:
            print('Mail Error')

    email = property(fget=get_email, fset=set_email)
    



