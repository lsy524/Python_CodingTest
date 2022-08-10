# 버블 정렬 알고리즘 개선 1 
# 교환 횟수(exchange)에 따라 중단 방식을 적용함 

def bubble_sort(data):
    n = len(data)

    for i in range(n - 1):
        exchange = 0
        for j in range(n - 1, i, -1):
            if data[j - 1] > data[j] :
                data[j - 1], data[j] = data[j], data[j - 1]
                exchange += 1

        if exchange == 0 :
            break

n = int(input())
data = [None] * n

for i in range(n):
    data[i] = int(input("data : "))

bubble_sort(data)


for i in range(n):
    print(f"data[{i}] = {data[i]}")