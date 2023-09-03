#Unpacking lists

numbers = [1,2,3]

first = numbers[0]
second = numbers[1]
third = numbers[2]

#the above code can be simplified as
first, second, third = numbers 

#case2
nums = [1,2,3,4,5,6,7,8,9,10]

first, second, *others = nums

print(first)  #1 will be printed 
print(second) #2 will be printed
print(others) #3-10 will be printed

first , *others, last = nums

print(first)
print(others)
print(last)