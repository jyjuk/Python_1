class PizzaMaker:

    def __make_pepperoni(self):
        return 'Визов метода def __make_pepperoni'

    def _make_barbecue(self):
        return 'Визов метода _make_barbecue'


maker = PizzaMaker()
print(maker._make_barbecue())
print(maker._PizzaMaker__make_pepperoni())


