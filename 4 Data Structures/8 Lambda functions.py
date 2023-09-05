#Lambda functions

items = [
  ('Product1',10),
  ('Product2',9),
  ('Product3',12),
]

items.sort(key=lambda item:item[1])
print(items)

#sample lambda functions

addition = lambda x,y : x + y
print(addition(5,5))

subtraction = lambda x,y : x - y
print(subtraction(10,5))

multi = lambda x,y,z : x * y * z
print(multi(5,5,5))

square = lambda x : x**2
print(square(10))

sq2 = lambda x,y : (x+y)**2
print(sq2(2,2))

sq3 = lambda x,y : x**2 + y**2
print(sq3(5,5))