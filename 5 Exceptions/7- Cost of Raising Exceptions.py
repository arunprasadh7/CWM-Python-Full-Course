# 7- Cost of Raising Exceptions

from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError('Age cannot be zero or less.')
    return 10/0


try:
	calculate_xfactor(-5)
except ValueError as e:
	print(e)
"""

# print('first code',timeit(code1, number = 10000))


code2 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError('Age cannot be zero or less.')
    return 10/0


try:
	calculate_xfactor(-5)
except ValueError as e:
	pass
"""

# print('Second code', timeit(code2, number = 10000))

code3 = """
def calculate_xfactor(age):
    if age <= 0:
    	return None
    return age/10


xfactor = calculate_xfactor(-5)
if xfactor == None:
	pass
"""

print(timeit(code3, number=10000))
