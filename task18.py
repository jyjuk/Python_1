class Robot:

    population = 0

    def __init__(self, name):
        self.name = name
        print(f'Робот {self.name} був створений')
        Robot.population += 1

    def destroy(self):
        Robot.population -= 1
        print(f'Робот {self.name} було знищено')

    def say_hello(self):
        print(f'Робот {self.name} вітає тебе')

    @classmethod
    def how_many(cls):
        print(f'{Robot.population} - ось скільки нас залишилося')


r2 = Robot('R2-D2')
r2.say_hello()
Robot.how_many()
r2.destroy()

