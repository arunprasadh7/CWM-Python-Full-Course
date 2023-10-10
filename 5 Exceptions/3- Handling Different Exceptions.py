# 3- Handling Different Exceptions

try:
    age = int(input('Age: '))
    xfactor = 10/age

except (ValueError, ZeroDivisionError):	#we can combine multiple exceptions seperated by commas 
    print('Age must be in numeric values.')

except ZeroDivisionError:
    print('Denominator cannot be zero')

else:
    print('No exceptions were thrown.')
