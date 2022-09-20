class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b


r1 = Rectangle(3, 5)
r2 = Rectangle(6, 1)
print(r1.area)
print(r2.area)
