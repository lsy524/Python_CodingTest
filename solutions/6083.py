x, y, z = map(int, input().split())

cnt = 0

for i in range(0, x):
    for j in range(0, y):
        for k in range(0, z):
            print(i, j, k)
            cnt += 1
print(cnt)