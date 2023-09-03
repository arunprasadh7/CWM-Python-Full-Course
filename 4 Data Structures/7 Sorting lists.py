# Sorting lists

numbers = [3, 51, 2, 8, 6]

numbers.sort()
print(numbers)

#sort in descending order 
numbers.sort(reverse=True)
print(numbers)
print('---------------------------------------------')

#sorted method - creates a new list 
numbers = [3, 51, 2, 8, 6]
print(sorted(numbers))
print(numbers)
print(sorted(numbers,reverse=True)) #sorted in reverse order
print('----------------------------------------')
#sorting a list of tuples
items = [
  ('Product1',10),
  ('Product2',9),
  ('Product3',12),
]

items.sort()  #by default this tuple is not sorted
print(items)

#here we can use a function to sort the list of tuples
items = [
  ('Product1',10),
  ('Product2',9),
  ('Product3',12),
]

def sort_item(item):
  return item[1]

items.sort(key=sort_item)
print(items)