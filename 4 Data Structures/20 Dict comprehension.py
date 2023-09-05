#Dict comprehension
values = []
for x in range(5):
  values.append(x*2)
print(values)

#using list comprehension
values = [x*2 for x in range(5)]
print(values)

#same can be used for dict comprehension
values = {x:x*2 for x in range(5)}
print(values)