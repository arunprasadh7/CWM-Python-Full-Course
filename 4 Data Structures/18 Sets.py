#Set - unordered collection of unique items,duplicates not allowed and are unordered

numbers = [1,2,2,3,3,3,4,4,5]

uniques = set(numbers) #duplicates will be removed
print(uniques)
uniques.add(6)
print(uniques)
uniques.remove(6)
print(uniques)
print(len(uniques))

#special set operators

first = {1,2,3,4}
second = {1,5}

print(first | second) #union - all items in both sets
print(first & second) #intersection - similar items in both sets
print(first - second) #Difference - items that are unique to first set and not present in secondset
print(first ^ second)#symmetric diff - items in first and second but not both

#checking existence of an item in set
if 3 in first:
  print('Yes')

if 10 not in first:
  print('No')

