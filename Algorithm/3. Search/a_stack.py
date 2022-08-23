stack = []

stack.append(5) # 삽입(5)
stack.append(2) # 5 - 삽입(2)
stack.append(3) # 5 - 2 - 삽입(3)
stack.append(7) # 5 - 2 - 3 - 삽입(7)
stack.pop()     # 5 - 2 - 3 - 삭제 
stack.append(1) # 5 - 2 - 3 - 삽입(1)
stack.append(4) # 5 - 2 - 3 - 1 - 삽입(4)
stack.pop()     # 5 - 2 - 3 - 1 - 삭제 

print(stack[::-1]) # 최상단 원소부터 출력 
print(stack)       # 최하단 원소부터 출력 