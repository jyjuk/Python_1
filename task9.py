class Person:

    def __init__(self, first_name, last_name, age):
        self.name = first_name
        self.second_name = last_name
        self.age = age

    def full_name(self):
        return f'{self.second_name} {self.name}'

    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False


p1 = Person('Jimi', 'Hendrix', 55)
print(p1.full_name())
print(p1.is_adult())
