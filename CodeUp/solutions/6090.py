import sys

a, m, d, n = map(int, sys.stdin.readline().split())

result = a

for i in range(1, n):
    result = result * m + d
 

print(result)