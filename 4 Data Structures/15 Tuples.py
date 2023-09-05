# tuples is a read only list.can't be modified

point = (1, 2)
print(type(point))
point = 1,2
print(type(point))
point = 1,
print(type(point))
point = () #empyt tuple

points = (1,2) + (3,4)
print(points)

mult = (1,2) * 3
print(mult)

#converting list to tuple
points = [1,2]
points = tuple([1,2])
print(points)
first = 'Hello World'
print(tuple(first))

#Similar to lists We can acess tuples using index 
points = (1,2,3,4,5,6,7,8,9)
print(points[0])
print(points[1])
print(points[:3])
print(points[3:5])

#tuple unpacking
points = (1,2,3)
x,y,z = points
print(x)
print(y)
print(z)

if 3 in points:
  print('Yes')

if 10 not in points:
  print('No')