import sys

a, d, n = map(int, sys.stdin.readline().split())

result = a

for _ in range(1, n):
    result += d 

print(result)