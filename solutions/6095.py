import sys 

d = [[0] * 20 for _ in range(20)]

n = int(sys.stdin.readline())

for i in range(n):
    x,y = map(int, sys.stdin.readline().split())
    d[x][y] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end =" ")
    print()
