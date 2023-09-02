#Types of functions
#1 - perform a task
#2 - calculate & return a value

#type1
def greet(name):
  print(f'Hi {name}.')

#type2
def get_greet(name):
  return f'Hi {name}.'

greet('Arun') #prints on terminal
print(greet('Arun')) #returns none- by default all functions return none value unless they are specified to return specific value

get_greet('Arun') #no print is used and thus does not appear on terminal

message = get_greet('Arun') #we can assign the return value to a variable and can use it later when required
print(message)