#Debugging in python

def multiply(*numbers):
  total = 1
  for number in numbers:
    total *= number
  return total

print('Start')
print(multiply(2,5,5,5,4))

