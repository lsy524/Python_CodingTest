# 5 2 3 7 , 1 4 ,
from collections import deque 

queue = deque()

queue.append(5) # 삽입(5)
queue.append(2) # 5 - 삽입(2)
queue.append(3) # 5 - 2 - 삽입(3)
queue.append(7) # 5 - 2 - 3 - 삽입(7)
queue.popleft() # 삭제 - 2 - 3 - 7
queue.append(1) # 2 - 3 - 7 - 삽입(1)
queue.append(4) # 2 - 3 - 7 - 1 - 삽입(4)
queue.popleft() # 삭제 - 3 - 7 - 1 - 4

print(queue)    # 먼저 들어온 순서대로 출력
queue.reverse() # 역순으로 바꾸기
print(queue)    # 나중에 들어온 원소부터 출력