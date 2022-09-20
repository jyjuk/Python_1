class City:
    latin = ['e', 'a', 'i', 'o', 'u']

    def __init__(self, name):
        self.name = name.title()

    def __str__(self):
        return f'{self.name}'

    def __bool__(self):
        for i in self.name:
            if self.name[-1] in self.latin:
                return False
            else:
                return True


p1 = City('new york')
print(p1)
print(bool(p1))
p2 = City('San frANCISco')
print(p2)
print(p2 == True)

