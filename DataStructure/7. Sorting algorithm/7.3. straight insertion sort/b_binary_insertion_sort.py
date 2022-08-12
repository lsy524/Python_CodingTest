# 이진 삽입 정렬
# 이진 검색법을 사용하여 삽입 정렬을 하면 이미 정렬을 마친 배열을 제외하고 원소를 삽입해야 할 위치를 검사하므로 비용을 줄임

# 이진 사입 정렬 알고리즘 구현 

def binary_insertion_sort(a):
    n = len(a)

    for i in range(1, n):
        key = a[i]
        pl = 0                              # 검색 범위의 맨 앞 원소 인덱스
        pr = i - 1                          # 검색 범위의 맨 끝 원소 인덱스 
        while True:
            pc = (pl + pr) // 2             # 검색 범위의 가운데 원소 인덱스 

            if a[pc] == key :               # 검색 성공 
                break
            elif a[pc] > key :              
                pr = pc - 1                 # 검색 범위를 뒤쪽 절반으로 좁힘 
            else :
                pl = pc + 1                 # 검색 범위를 앞쪽 절반으로 좁힘 

            if pl > pr : 
                break
        
        pd = pc + 1 if pl <= pr else pr + 1 # 삽입해야 할 위치의 인덱스 

        for j in range(i, pd, -1):
            a[j] = a[j - 1]
        a[pd] = key 




num = int(input("elements : "))
x = [None] * num 

for i in range(num):
    x[i] = int(input(f"x[{i}] : "))


binary_insertion_sort(x)

for i in range(len(x)):
    print(f"x[{i}] = {x[i]}")