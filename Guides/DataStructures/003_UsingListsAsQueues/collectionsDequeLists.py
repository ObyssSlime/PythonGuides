# first in, first out
from collections import deque

queue = deque(["john", "jack", "harry"])
print(queue)

queue.append("barry") # append, add item from last queue
print(queue)

queue.popleft() # popleft, remove item from first queue
print(queue)
