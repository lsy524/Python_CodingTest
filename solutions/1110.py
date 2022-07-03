import sys 

x = int(sys.stdin.readline())

y = x 
cnt = 0

while True :
    a = y // 10
    b = y % 10
    c = (a + b) % 10 
    y = (b * 10) + c 
    
    cnt += 1
    
    if y == x :
        break
print(cnt)