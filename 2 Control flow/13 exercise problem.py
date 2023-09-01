# print all even numbers between 1 and 10 and display the total count of even numbers

#using for loop

count = 0
for number in range(1,10):
  if number % 2 == 0:
    print(number)
    count += 1

print(f'We have {count} numbers.')

#using while loop

num = 1
count = 0
while num < 10:
  if num %2 == 0:
    print(num)
    count += 1
  num += 1
print(f'We have {count} values.')