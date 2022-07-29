import sys 

h, w = map(int, sys.stdin.readline().split())

table = [[0] * w for _ in range(h)]

n = int(sys.stdin.readline())

for _ in range(n):
    l, d, x, y = map(int, sys.stdin.readline().split())
    
    for j in range(l):
        if d == 0:
            table[x - 1] [y - 1 + j] = 1
        else :
            table[x - 1 + j][y - 1] = 1

for i in range(h):
    for j in range(w):
        print(table[i][j], end = " ")
    print()