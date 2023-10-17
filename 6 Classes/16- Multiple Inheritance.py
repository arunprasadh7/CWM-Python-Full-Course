# 16- Multiple Inheritance

class Employee:
    def greet(self):
        print('Employee Greet')

class Person:
    def greet(self):
        print('Person Greet')

class Manager(Employee, Person):
    pass

m1 = Manager()
m1.greet()

#good example of multiple inheritance

class Flyer:
    pass

class Swimmer:
    pass

class FlyingFish(Flyer, Swimmer):
    pass