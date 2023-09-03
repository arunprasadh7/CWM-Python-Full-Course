#Finding items in a list

num = [1,2,3,4,5]

#index
print(num.index(1))
print(num.index(3))
#print(num.index(8)) #if the value is not present throws errror
#we can use that with the if condition to prevent running into error

if 8 in num:
  print(num.index(8))

#count
print(num.count(1))