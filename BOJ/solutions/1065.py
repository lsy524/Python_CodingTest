import sys 

def hansu(x):
    cnt = 0
    for i in range(1, x+1):
        numlist = list(map(int, str(i)))
        if i < 100 :
            cnt += 1 
        elif numlist[0] - numlist[1] == numlist[1]  - numlist[2]:
            cnt += 1
    return cnt

x = int(sys.stdin.readline())

print(hansu(x))