class Vector:
    def __init__(self, *args):
        self.values = []
        for arg in args:
            if isinstance(arg, int):
                self.values.append(arg)

    def __str__(self):
        if self.values:
            return f'Вектор {tuple(sorted(self.values))}'
        else:
            return 'Вектор пустий'


v1 = Vector(1, 'hj', 52, 'n', 3)
print(v1)
v2 = Vector()
print(v2)

