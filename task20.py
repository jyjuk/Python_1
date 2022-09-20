class Person:

    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname
        self.gender = gender

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        if value == 'female':
            self.__gender = value
        elif value == 'male':
            self.__gender = value
        else:
            print('Я не знаю що Ви мали на увазі. Нехай буде хлопчик')
            self.__gender = 'male'

    def __str__(self):
        if self.gender == 'male':
            return f'Громадянин {self.surname} {self.name}'
        else:
            return f'Громадянка {self.surname} {self.name}'


p1 = Person('Chuk', 'Norris')
print(p1)
p2 = Person('Mila','Kunis', 'female')
print(p2)
p3 = Person('Obi', 'Kenobi', True)
print(p3)

