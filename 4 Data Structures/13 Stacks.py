#Stacks
#The last book we put on top of the stack is the first we can remove
#LIFO - Last In First Out
#eg browser keeps our browsing session in a stack

browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
print('redirect',browsing_session[-1])
if not browsing_session:
  print('disable')
