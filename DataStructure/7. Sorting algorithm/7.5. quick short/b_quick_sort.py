# 퀵 정렬 알고리즘 구현 

def qsort(a, left, right):
    pl = left
    pr = right 
    x = a[(left + right) // 2]

    while pl <= pr:
        while a[pl] < x : pl += 1
        while a[pr] > x : pr -= 1

        if pl <= pr :
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr : qsort(a, 0, pr)
    if pl < right : qsort(a, pl, right)

def quick_sort(x):
    qsort(x, 0, len(x) - 1)

# num = int(input("Elements : "))
# x = [None] * num

# for i in range(num):
#     x[i] = int(input(f"x[{i}]"))

x = [5,8,4,2,6,1,3,9,7]

quick_sort(x)

print("==============================")

for i in range(len(x)):
    print(f"x[{i}] = {x[i]}")