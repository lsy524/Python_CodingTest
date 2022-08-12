# 셸 정렬 알고리즘 구현 

def shell_sort(a):

    n = len(a)
    h = n // 2                 

    while h > 0:
        for i in range(h, n):
            j = i - h           
            tmp = a[i]
            while j >= 0 and a[j] > tmp :
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp 
        h //= 2

num = int(input("elements : "))
data = [None] * num 

for i in range(num) :
    data[i] = int(input(f"data[{i}] : "))

shell_sort(data)

for i in range(num):
    print(f"data[{i}] = {data[i]}")