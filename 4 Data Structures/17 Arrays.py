#arrays - similar to lists , but are faster and require less memory 
# use arrays only when dealing with a very large sequence of numbers or when encountering any performance problems
#we can see the difference between arrays and lists only when we are dealing with very large sequence of numbers , greater than 10k

from array import array

numbers = array('i',[1,2,3]) #i means only int can be used, we can't mix datatypes as in lists

#we can perfomr methods in array similar to list
numbers.append(4)
print(numbers)
numbers.insert(0,0)
print(numbers)
numbers.pop()
print(numbers)
numbers.remove(0)
print(numbers)
