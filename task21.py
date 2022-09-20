class Vector:

    values = []

    def __init__(self, *args):
        for arg in args:
            if isinstance(arg, int):
                self.values = args

    def __str__(self):
        if len(self.values):
            return f'Вектор {tuple(self.values)}'
        else:
            return 'пустий вектор'


v1 = Vector(1, 2, 3)
print(v1)
v2 = Vector()
print(v2)

