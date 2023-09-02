# keyword arguments

def increment(number, by):
  return number + by

result = increment(2,1)
print(result)

#The above code can be written as
print(increment(5,2))

#We can mention the keyword for the above args
print(increment(5,by=2)) # by= is the keyword for the arg 2

#case 2 

def full_name(first_name,last_name):
  return f'Hello {first_name} {last_name}.'

print(full_name(first_name='Arun', last_name='Prasadh'))
print(full_name(last_name='Warden', first_name='Arc')) #order of insertion does not matter while using keyword args

