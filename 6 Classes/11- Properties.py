# 11- Properties

class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        self.__price

    def set_price(self,value):
        if value < 0:
            raise ValueError('Price cannot be negative.')
        self.__price = value


p1 = Product(-50)
# p2 = Product(100)
