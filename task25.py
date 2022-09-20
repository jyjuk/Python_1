class Quadrilateral:

    def __init__(self, width, height=None):
        self.width = width
        if (height):
            self.height = height
        else:
            self.height = width

    def __str__(self):
        if self.width == self.height:
            return f'Куб розміром {self.width} x {self.height}'
        else:
            return f'Прямокутник розміром {self.width} x {self.height}'

    def __bool__(self):
        if self.width == self.height:
            return True
        else:
            return False


q1 = Quadrilateral(10)
print(q1)
print(bool(q1))
q2 = Quadrilateral(3, 5)
print(q2)
print(q2 == True)


