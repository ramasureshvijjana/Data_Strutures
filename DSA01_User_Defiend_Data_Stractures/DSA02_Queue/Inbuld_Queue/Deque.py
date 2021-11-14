'''
1. We have all functions in collections.deque as like as list.
2. This is inbuld Queue in python.

'''

from collections import deque

que = deque()

# Left join queue
que.appendleft(10) # Add left side
que.append(60)     # Add right side
que.append(50)
que.appendleft(20)

# View que now
print(que)

# Now remove one by one
que.pop()     # Remove right side
print(que)

que.pop()
print(que)

que.popleft() # Remove left side
print(que)

que.popleft()
print(que)
