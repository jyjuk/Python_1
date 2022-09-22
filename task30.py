class NewInt(int):

    def repeat(self, number=2):
        return int(str(self)*number)

    def to_bin(self):
        return bin(int(self))


a = NewInt(9)
print(a.repeat())
d = NewInt(a + 5)
print(d.repeat(3))
b = NewInt(NewInt(7) * NewInt(5))
print(b.to_bin())





