#Keyword arguments - **kwargs
# is used to pass a variable number of keyword arguments (key-value pairs) to a function.
# collects the keyword arguments into a dictionary, where the keys are the argument names and the values are the corresponding values.

def save_user(**user):
  print(user)
  print(user.keys())
  print(user.values())
  print(user.items())

save_user(id=1,name='Arun',age=26)
