#filter ()

items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 12),
]

#to filter the products where price >= 10

price = filter(lambda item:item[1] >= 10, items)
print(price)  #returns x object that can be looped over 

for i in price:
  print(i) #returns only products with price >= 10

#alternate : we can convert the filter function to list

filtered_price = list(filter(lambda item:item[1] >= 10, items))
print(filtered_price)