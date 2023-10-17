# 12- Inheritance
# Animal  - parent, base class
# Mammal, Fish - child , sub class

class Animal:   #parent class
    def __init__(self):
        self.age = 1

    def eat(self):
        print('Eating')

class Mammal(Animal):   #child class
    def walk(self):
        print('Walking')

class Fish(Animal):     #child class
    def swim(self):
        print('Swimming')

a = Animal()
a.eat()

m = Mammal()
m.eat()
m.walk()
print(m.age)

f = Fish()
f.eat()
f.swim()
print(f.age)