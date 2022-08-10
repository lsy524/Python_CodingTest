# 버블 정렬 알고리즘 구현 

# 버블 정렬 
def bubble_sort(data):
    n = len(data)

    for i in range(n - 1):
        # 패스 
        for j in range(n - 1, i, -1):
            if data[j - 1] > data[j] :
                data[j - 1], data[j] = data[j], data[j - 1]

x = int(input())
data = [None] * x

for i in range(x):
    data[i] = int(input(f"data[{i}] : "))

bubble_sort(data)

print("=========================")

for i in range(x):
    print(f"data[{i}] = {data[i]}")