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

    def __add__(self, other):
        if isinstance(other, int):
            b = [i + other for i in self.values]
            return Vector(*b)
        elif isinstance(other, Vector):
            if len(self.values) == len(other.values):
                b = [sum(i) for i in zip(self.values, other.values)]
                return Vector(*b)
            else:
                return 'Складання Векторів різної довжини недопустий'
        else:
            return f'Неможливо скласти Вектор з {other}'

    def __mul__(self, other):
        if isinstance(other, int):
            b = [i * other for i in self.values]
            return Vector(*b)
        elif isinstance(other, Vector):
            if len(self.values) == len(other.values):
                b = [i[0]*i[1] for i in zip(self.values, other.values)]
                return Vector(*b)
            else:
                return 'Множення Векторів різної довжини недопустий'
        else:
            return f'Неможливо множити Вектор з {other}'


v1 = Vector(2, 5, 1, 'gh', 67, 'error', 12, 43, 9)
print(v1)
print(v1 + 7)
v2 = Vector(45, 76, 1, 'f')
v3 = Vector('df', 34, 'a', 45, 2)
print(v2)
print(v3)
print(v3 + 'fg')
print(v3 * 2)
print(v3 * v2)
print(v3 * 'hi')







