x, y = map(int, input().split())

coin = []
result = 0

for i in range(x):
    coin.append(int(input()))

coin.reverse()

for i in coin:
    result += (y // i)
    y %= i

print(result)

