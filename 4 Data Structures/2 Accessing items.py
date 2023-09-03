#Accessing items

letters = ['a','b','c','d']

print(letters[0])
print(letters[-1])

letters[0] = 'A'

print(letters)
print(letters[0:3])
print(letters[:3])
print(letters[0:])
print(letters[:])
print(letters[::2])
print(letters[::-1])

numbers = list(range(20))

print(numbers[::-1])
print(numbers[::-2])