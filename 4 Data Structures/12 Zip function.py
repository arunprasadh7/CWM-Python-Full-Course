#zip()

list1 = [1,2,3]
list2 = [10,20,30]

combined_list = zip(list1,list2)
print(combined_list)  #returns a zip object that can be iterated for values
for x in combined_list:
  print(x)

#we can turn it to a list

combined_list = list(zip(list1,list2))
print(combined_list)

#we can add any number of args inside the zip function

combined_list = list(zip('Arun',list1,list2))
print(combined_list)