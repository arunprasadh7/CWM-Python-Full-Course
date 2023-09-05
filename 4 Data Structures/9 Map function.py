# Map function

items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 12),
]

# to print the values alone in a seperate list we can usually use a loop
prices = []
for item in items:
  prices.append(item[1])

print(prices)

#we can use map function to do the same

prices = map(lambda item:item[1], items)
print(prices) #this will print a price object 

#the price object can be looped to get the values
for price in prices:
  print(price)

#we can typecast the map function to list to skip the looping 

prices = list(map(lambda item:item[1], items))
print(prices)
