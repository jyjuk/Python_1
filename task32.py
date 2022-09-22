class Initialization:

    def __init__(self, capacity, food):
        if not isinstance(capacity, int):
            print("Кількість людей має бути ціле число")
        else:
            self.capacity = capacity
            self.food = food


class Vegetarian(Initialization):

    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f'{self.capacity} людей вибирають не Їсти мясо. Вони віддають перевагу {self.food}'


class MeatEater(Initialization):

    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f'{self.capacity} людей їсть мясо. Окрім мяса вони також їдять {self.food}'


class SweetTooth(Initialization):

    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f'Любителів солодкого є {self.capacity}. Окрім солодкого вони надають перевагу {self.food}'

    def __eq__(self, other):
        if isinstance(other, int):
            if other == self.capacity:
                return True
            else:
                return False
        elif isinstance(other, (Vegetarian, MeatEater)):
            if other.capacity == self.capacity:
                return True
            else:
                return False
        else:
            return f'Неможливо порівняти солодкоїжок з {other}'

    def __lt__(self, other):
        if isinstance(other, int):
            if self.capacity < other:
                return True
            else:
                return False
        elif isinstance(other, (Vegetarian, MeatEater)):
            if self.capacity < other.capacity:
                return True
            else:
                return False

        else:
            return f'Неможливо порівняти солодкоїжок з {other}'

    def __gt__(self, other):
        if isinstance(other, int):
            if self.capacity > other:
                return True
            else:
                return False
        elif isinstance(other, (Vegetarian, MeatEater)):
            if self.capacity > other.capacity:
                return True
            else:
                return False

        else:
            return f'Неможливо порівняти солодкоїжок з {other}'


v_first = Vegetarian(10000, ['горіхи', 'овочі', 'фрукти'])
print(v_first)
v_second = Vegetarian([23], ['nothing'])
m_first = MeatEater(15000, ['смажена кртoпля', 'риба'])
print(m_first)
s_first = SweetTooth(30000, ['морозиво', 'шоколад', 'чіпси'])
print(s_first)
print(s_first > v_first)
print(30000 == s_first)
print(s_first == 25000)
print(100000 < s_first)
print(100 < s_first)
