# 셸 정렬 알고리즘 구현(h * 3 + 1 수열 사용)

def shell_sort(a):
    n = len(a)
    h = 1

    while h < n // 9 :
        h = h * 3 + 1

    while h > 0 :
        for i in range(h, n):
            j = i - h 
            tmp = a[i]

            while j  >= 0 and a[j] > tmp :
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp
        h //= 3


x = [8,4,1,2,7,6,3,5]

shell_sort(x)

for i in range(len(x)):
    print(x[i])