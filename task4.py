class Counter:

    def start_from(self, value=0):
        self.value = value

    def increment(self):
        self.value += 1

    def display(self):
        print(f'Поточне значення = {self.value}')

    def reset(self):
        self.value = 0


c1 = Counter()
c1.start_from()
c1.increment()
c1.display()
c1.increment()
c1.display()
c1.reset()
c1.display()

c2 = Counter()
c2.start_from(3)
c2.display()
c2.increment()
c2.display()
