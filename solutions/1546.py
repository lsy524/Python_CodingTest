import sys 

x = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

maxx = max(a)
result = 0

for i in a :
    result += i / maxx * 100
    
print(result / len(a))