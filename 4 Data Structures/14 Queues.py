# queue  - resembles a que in real world
# FIFO - First In First Out

# queue = [1,2,3,4]

from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()  # removes the first item from the list,only available with deque
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)
if not queue:
    print('empty')
