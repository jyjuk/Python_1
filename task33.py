class Wallet:

    def __init__(self, currency, balance):
        if not isinstance(currency, str):
            raise TypeError('Невірний тип валюти')
        if len(currency) != 3:
            raise NameError('Невірна довжина назви валюти')
        if not currency.isupper():
            raise ValueError('Назва має складатися з великих сиволів')
        self.currency = currency
        self.balance = balance

    def __eq__(self, other):
        if isinstance(other, Wallet):
            if other.currency == self.currency:
                return other.balance == self.balance
            else:
                return 'Не можна порівнювати різні валюти'
        else:
            raise TypeError(f'Wallet не підтримує порівняння з {other}')

    def __add__(self, other):
        if isinstance(other, Wallet) and self.currency == other.currency:
            return Wallet(self.currency, self.balance + other.balance)
        else:
            raise ValueError('Дана операція заборонена')

    def __sub__(self, other):
        if isinstance(other, Wallet) and self.currency == other.currency:
            return Wallet(self.currency, self.balance - other.balance)
        else:
            raise ValueError('Дана операція заборонена')


wallet1 = Wallet('USD', 50)
wallet2 = Wallet('UAH', 100)
wallet3 = Wallet('UAH', 150)
#wallet4 = Wallet(12, 150)
#wallet5 = Wallet('qwerty', 150)
#wallet6 = Wallet('abc', 150)
print(wallet2 == wallet3)
#print(wallet2 == 100)
print(wallet2 == wallet1)
wallet7 = wallet2 + wallet3
print(wallet7.currency, wallet7.balance)
#wallet2 + 47
