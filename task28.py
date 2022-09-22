class Building:

    def __init__(self, floors):
        self.floors = [None] * (floors+1)

    def __setitem__(self, key, value):
        self.floors[key] = value

    def __getitem__(self, items):
        if items < len(self.floors):
            return self.floors[items]
        else:
            return 'Overr!!!'

    def __delitem__(self, key):
        self[key] = None


iron_building = Building(22)
iron_building[0] = 'Recepcion'
iron_building[1] = 'Oscorp Industries'
iron_building[2] = 'Stark Industries'
print(iron_building[2])
del iron_building[2]
print(iron_building[0])
print(iron_building[1])
print(iron_building[2])
print(iron_building[23])


