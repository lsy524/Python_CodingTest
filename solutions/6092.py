n = int(input())

data = list(map(int, input().split()))

result = [0 for i in range(24)]

for i in range(n):
    result[data[i]] += 1

for i in range(1, len(result)):
    print(result[i], end=" ")
