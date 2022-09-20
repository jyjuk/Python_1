class Money:

    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, dollar):
        if isinstance(dollar, int) and int(dollar) > 0:
            self.total_cents = dollar * 100 + self.cents
        else:
            print('Error dollars!')

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, cents):
        if isinstance(cents, int) and int(cents) < 100:
            self.total_cents = self.dollars * 100 + cents

    def __str__(self):
        return f'Ваш стан складає {self.dollars} доларів і {self.cents} центів'


bill = Money(101, 99)
print(bill)
print(bill.dollars, bill.cents)
print(bill.total_cents)
bill.dollars = 666
print(bill)
bill.cents = 12
print(bill)
