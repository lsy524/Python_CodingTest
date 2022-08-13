# 배열을 두 그룹으로 나누기

def partition(a):
    # 배열을 나누어 출력
    n = len(a)
    pl = 0                                          # 왼쪽 커서 
    pr = n - 1                                      # 오른쪽 커서
    x = a[n // 2]                                   # 피벗(가운데 원소)

    # 배열 a를 피벗 x로 나눔 
    while pl <= pr :
        while a[pl] < x : pl += 1
        while a[pr] > x : pr -= 1
        
        if pl <= pr :
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
        
        print(f"pivot = {x}")

        print(f"pivot under = {a[0 : pl]}")         # a[0] ~ a[pl - 1]

        if pl > pr + 1:     
            print(f"pivot same = {a[pr + 1 : pl]}") # a[pr + 1] ~ a[pl - 1]

        print(f"pivot over = {a[pr + 1 : n]}")      # a[pr + 1] ~ a[n - 1]



num = int(input("Elements : "))
x = [None] * num

for i in range(num):
    x[i] = int(input(f"x[{i}]"))

partition(x)