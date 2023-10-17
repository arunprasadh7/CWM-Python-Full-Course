# 14- Method Overriding - over riding a method defined in the base class

class Animal:
    def __init__(self):
        print('Animal constructor')
        self.age = 1

    def eat(self):
        print('Eating')

class Mammal(Animal):
    def __init__(self):
        print('Mammal constructor')
        self.weight = 2
        super().__init__()


    def walk(self):
        print('Walking')

m1 = Mammal()
print(m1.age)
print(m1.weight)

