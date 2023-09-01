# Chaining comparison operators

# age should be between 18 and 65

#method1
age = 22
if age >= 18 and age <= 65:
  print('Eligible')

#method2
age = 22
if 18 <= age <= 65:
  print('Eligible')