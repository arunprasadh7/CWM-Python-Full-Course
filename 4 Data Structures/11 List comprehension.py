# List comprehension

items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 12),
]

# map function
price = list(map(lambda item: item[1], items))
print(price)
# using list comprehension
price = [item[1] for item in items]
print(price)

print('------------------------------------')
# filter function
price = list(filter(lambda item: item[1] >= 10, items))
print(price)
# using list comprehension
price = [item for item in items if item[1] >= 10]
