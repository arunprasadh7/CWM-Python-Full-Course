#String methods

course = '   python programming'

print(course.lower())
print(course.upper())
print(course.title())
print(course.capitalize())

print(course.strip())
print(course.rstrip())
print(course.lstrip())

print(course.find('pro'))
print(course.find('zoo'))
print(course.find('p',4))
print(course.find('o',3,10))
print(course.index('p'))

print(course.replace('p','j'))

print(course.isalpha())
print(course.isalnum())

print('pro' in course)
print('bro' in course)
print('bro' not in course)
print('bro' in course)
