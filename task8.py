class Zebra:

    zebra = 0

    def which_stripe(self):
        if self.zebra == 0:
            print('Полоска біла')
            self.zebra = 1
        else:
            print('Полоска чорна')
            self.zebra = 0


z1 = Zebra()
z1.which_stripe()
z1.which_stripe()
z1.which_stripe()
z2 = Zebra()
z2.which_stripe()
