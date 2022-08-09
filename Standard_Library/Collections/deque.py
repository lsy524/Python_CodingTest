from collections import deque

data = deque([2,3,4])

data.appendleft(1)  
print(data) # deque([1, 2, 3, 4])

data.append(5)
print(data) # deque([1, 2, 3, 4,5]) 