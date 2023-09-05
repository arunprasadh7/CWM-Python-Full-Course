#swapping variables

x = 10
y = 11

#generally we can swap values of x and y using a third variable z
z = x
x = y
y = z
print(x,y)

#in python we can swap using simple tuple unpacking
a = 5
b = 4
a,b = b,a #this is  tuple unpacking;b,a is a tuple; b,a = (b,a) 
print(a,b)

c,d,e = 1,2,3
print(c)
print(d)
print(e)