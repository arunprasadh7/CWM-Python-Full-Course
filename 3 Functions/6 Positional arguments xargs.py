#xargs/*args - positional arguments
# is used to pass a variable number of non-keyword (positional) arguments to a function.
# When you use *args in a function definition, it collects all the additional positional arguments into a tuple.

#case1- two args
def multiply(x,y):
  return x * y

print(multiply(2,2))

#case2- more than 2 args

def product(*numbers):
  return numbers 

print(product(2,2,2,2,2))

#the above code can be modified as 
def product(*numbers):
  total = 1
  for number in numbers:
    total = number * total
  return total

print(product(2,2,2,2,2))
print(product(5,5,5,5))
print(product(10,10,10))

#case3- sum function

def addition(*numbers):
  total = 0
  for number in numbers:
    total += number
  return total

print(addition(5,5,5,5,5))
print(addition(10,10,10,10,10))

