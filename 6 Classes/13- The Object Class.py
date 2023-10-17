# 13- The Object Class
# class object is the base class for all objects in python

class Animal:   #parent class
    def __init__(self):
        self.age = 1

    def eat(self):
        print('Eating')

class Mammal(Animal):
    def walk(self):
        print('Walk')


m = Mammal()
print(isinstance(m, Mammal))
print(isinstance(m, object))

a = Animal()
print(isinstance(a, Animal))
print(isinstance(a, object))

print(issubclass(Mammal, Animal))
print(issubclass(Animal, Mammal))
print(issubclass(Animal, object))