#Generator expression 
#generator dont store values in memory and can be accessed through iteration

values = [x*2 for x in range(10)]   #this is a list
for x in values:
  print(x)

#generator 
values = (x*2 for x in range(10)) #() generator
print(values) #returns generator object
for x in values:  #generator obj is iterable
  print(x)

print('-------------------------')

#checking size of an object- generators take less memory compared to lists
from sys import getsizeof

values = (x*2 for x in range(1000)) #() generator with size 1000
print('get:',getsizeof(values)) #takes less memory 208 bytes

values = [x*2 for x in range(1000)]#list with size 1000
print('list:',getsizeof(values))  #takes 8856 bytes


values = (x*2 for x in range(100000))
print('get',getsizeof(values))#takes same memory of 208 despite increased range

values = [x*2 for x in range(100000)]#list with size 100000
print('list:',getsizeof(values))  #takes 800984 bytes