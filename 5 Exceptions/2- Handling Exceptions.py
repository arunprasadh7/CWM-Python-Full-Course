# 1- Handling xceptions

try:
    age = int(input('Age:'))
except ValueError as e:
    print('Age must be in numeric values.')
    print(e)
    print(type(e))
else:
    print('No exceptions were thrown.')
    print('Execution continues')
