#Ternary operator

age = 22

#method 1
if age >= 18:
  print('ELigible.')
else:
  print('Not Eligible.')

#method2:
if age >= 18:
  message = 'Eligible'
else:
  message = 'Not eligible.'
print(message)

#method 3: using ternary operator
message = 'Eligible' if age >= 18 else 'Not eligible'
print(message)