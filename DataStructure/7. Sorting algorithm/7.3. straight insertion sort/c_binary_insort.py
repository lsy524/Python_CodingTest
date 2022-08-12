# 이진 삽입 정렬 알고리즘 구현(bisect.insort 사용)


from bisect import insort

def binary_inserction_sort(a):
    for i in range(1, len(a)):
        # bisect.insort(a, x, lo = 0, hi = len(a))
        # a가 이미 정렬된 상태를 유지하면서 a[lo] ~ a[hi]사이에 x를 삽입한다. 만약 a안의 x와 같은 값을 갖는 원소가 여러개 있으면 가장 오른쪽 위치에 삽입
        insort(a, a.pop(i), 0, i)
        


x = [6,4,3,7,1,2,8,9]

binary_inserction_sort(x)

for i in range(len(x)):
    print(x[i])