import sys

a, r, n = map(int, sys.stdin.readline().split())

result = a

for i in range(1, n):
    result *= r

print(result)
