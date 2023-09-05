#Dict - key value pairs
#we can only use immutable types for keys - strings, numbers

point = {'x':1, 'y':2}
point = dict(x=1, y=2)
print(point['x'])
print(point['y'])
#assigning values
point['x'] = 10
print(point['x'])
print(point)
point['z'] = 20
print(point)

#if we use an invalid key we will get an error, 
#print(point['a'])

if 'a' in point:
  print(point['a'])

#get method
print(point.get('a')) #returns none if the key is not present in dict
print(point.get('y'))
#get method with default value
print(point.get('a',0)) #returns 0 if a is not present in dict
print(point.get('y',0)) #y is present and thus returns y value

#delete item
del point['x']
print(point)

#looping over dict
for x in point:
  print(x)

for key in point.keys(): #returns keys only
  print(key)

for value in point.values(): #returns values only
  print(value)

for key,value in point.items(): #return both key&value as tuple
  print(key,value)