#Unpacking operator *

numbers = [1,2,3]
print(numbers)
print(*numbers) #unpacked list numbers

values = list(range(5))
print(values)
values = [*range(5)]
print(values)
values = [*range(10), *'Hello Arun']
print(values)

#unpacking multiple lists
first = [1,2]
second = [3]
values = [*first, *'Arun', *second, *'Prasadh']
print(values)

#unpacking dictionaries
one = {'x':1}
two = {'x':10, 'y':20}
combined = {**one, **two, 'z':1}
print(combined)