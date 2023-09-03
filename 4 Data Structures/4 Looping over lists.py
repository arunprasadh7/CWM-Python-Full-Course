# Looping over lists

letters = ['a', 'b', 'c', 'd']

# method 1 - using for loop

for letter in letters:
    print(letter)

# if we want the list items along with index value we can use enumerate
# enumerate returns a tuple(index,value) containing index and values
for letter in enumerate(letters):
    print(letter)

#we can unpack tuples similar to lists

for letter in enumerate(letters):
    print(letter[0],letter[1])

#the above code can be simplified as 

for index, value in enumerate(letters):
    print(index, value)