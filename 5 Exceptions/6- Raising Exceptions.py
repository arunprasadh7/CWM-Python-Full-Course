# 6- Raising Exceptions

def calculate_xfactor(age):
    if age <= 0:
        raise ValueError('Age cannot be zero or less.')
    return 10/0


try:
	calculate_xfactor(-5)
except ValueError as e:
	print(e)