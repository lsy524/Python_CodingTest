# 동북서남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

x, y = 2, 2

for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    print(f"({nx}, {ny})")

# for i in range(5):
#     for j in range(5):
#         print(f"({i}, {j})", end= " ")
#     print()
    