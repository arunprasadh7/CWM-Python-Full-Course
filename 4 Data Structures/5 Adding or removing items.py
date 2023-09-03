#Adding or removing items in lists

letters = ['a','b','c','d']

#add

letters.append('e') #adds e to last 
print(letters)
letters.insert(0,'-') #inserts the mentioned value to specified index
print(letters)

#removing
print('Removing')
#pop - can be used if index of item is known
letters.pop() #by default removes last list item
print(letters)
letters.pop(0) #removes item from 0 index
print(letters)
#remove - used when  index is unknown
letters.remove('b') # removes the first occurence of b
print(letters)
#del - can be used to remove a range of items
del letters[0:3 ] #values in the index range will be removed
#clear - can be used to remove all items in the list
letters.clear() #removes entire list