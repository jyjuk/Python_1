import math


class Point:

    def set_coordinats(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, other):
        if not isinstance(other, Point):
            print('Передана не точка')
        else:
            return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


p1 = Point()
p2 = Point()
p1.set_coordinats(1, 2)
p2.set_coordinats(4, 6)
d = p1.get_distance(p2)
print(d)
p1.get_distance(10)

