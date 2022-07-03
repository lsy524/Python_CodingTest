import sys 

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

result = list(map(int, str(a * b * c)))

for i in range(10):
    print(result.count(i))