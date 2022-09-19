class Laptop:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = self.brand + ' ' + self.model


hp = Laptop('hp', '15-bw0xx', 57000)
print(hp.price)
print(hp.laptop_name)
laptop1 = Laptop("Apple", 'MacBook', 62000)
laptop2 = Laptop('Dell', 'Precision 3510', 61250)
