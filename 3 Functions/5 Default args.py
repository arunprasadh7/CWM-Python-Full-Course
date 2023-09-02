# Default args - mentioned in function
#default arg must always be mentioned at last

#case1
def increment(number,by=2): #by=2 is default arg
  return number + by

print(increment(5)) #second arg not mentioned,applies default arg
print(increment(5,5))#second arg specified and uses that value
