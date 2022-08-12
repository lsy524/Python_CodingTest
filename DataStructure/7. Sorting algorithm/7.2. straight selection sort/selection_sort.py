# 단순 선택 정렬 알고리즘 구현 
# 비교 횟수 : (n**2 - n) / 2번 
# 서로 이웃하지 않는 떨어져 있는 원소를 교환하므로 안정적이지 않음 -> 똑같은 원소가 2개 있다면 해당 원소보다 큰 원소를 두번 반복해야함 


def selection_sort(x):
    n = len(x)
    
    for i in range(n - 1):
        min = i                     # 정렬할 부분에서 가장 작은 원소의 인덱스 
        for j in range(i + 1, n):
            if x[j] < x[min]:
                min = j 
        x[i], x[min] = x[min], x[i] # 정렬한 부분에서 맨 앞의 원소의 가장 작은 원소를 교환


x = int(input("elements : "))
data =[None] * x

for i in range(x):
    data[i] = int(input(f"data[{i}] : "))

selection_sort(data)

for i in range(x):
    print(f"data[{i}] = {data[i]}")