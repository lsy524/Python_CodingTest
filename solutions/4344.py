import sys 

x = int(sys.stdin.readline())

for i in range(x):
    a = list(map(int, sys.stdin.readline().split()))

    result = 0
    cnt = 0
    avg = 0
    
    for k in range(1, len(a)):
        result += a[k]
        
    avg = result / a[0]
    
    for j in range(1, len(a)):
        if a[j] > avg :
            cnt += 1
    print("%.3f" %(cnt / a[0] * 100)+"%")