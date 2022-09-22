class Transport:

    def __init__(self, brand, max_speed, kind=None):
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind

    def __str__(self):
        return f'Тип транспорта {self.kind} марки {self.brand} може розвивати максимальну швидкість {self.max_speed} км/год'


class Car(Transport):

    def __init__(self, brand, max_speed, mileage, gasoline_residue):
        super().__init__(brand, max_speed, kind='Car')
        self.mileage = mileage
        self.__gasoline_residue = gasoline_residue

    @property
    def gasoline(self):
        return f'Залишилося бензину на {self.__gasoline_residue} км'

    @gasoline.setter
    def gasoline(self, value):
        if isinstance(value, int):
            self.__gasoline_residue = self.__gasoline_residue + value
            print(f'Обєм палива збільшено на {value}л і становить {self.__gasoline_residue}л')
        else:
            print('Помилка заправки авто')


class Boat(Transport):

    def __init__(self, brand, max_speed, owners_name):
        super().__init__(brand, max_speed, kind='Boat')
        self.owners_name = owners_name

    def __str__(self):
        return f'Дана лодка марки {self.brand} є власністю {self.owners_name}'


class Plane(Transport):

    def __init__(self, brand, max_speed, capacity):
        super().__init__(brand, max_speed, kind='Plane')
        self.capacity = capacity

    def __str__(self):
        return f'Самольот марки {self.brand} вміщає в себе {self.capacity} людей.'


transport = Transport('Telega', 10)
print(transport)
bike = Transport('shkolnik', 20, 'bike')
print(bike)
first_plane = Plane('Virgin Atlantic', 700, 450)
print(first_plane)
first_car = Car('bmw', 230, 75000, 300)
print(first_car)
print(first_car.gasoline)
first_car.gasoline = 20
print(first_car.gasoline)
second_car = Car('Audi', 230, 70000, 130)
second_car.gasoline = [None]
first_boat = Boat('Yamaha', 40, 'Petr')
print(first_boat)





















