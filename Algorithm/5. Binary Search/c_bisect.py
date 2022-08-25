# 이진 탐색 라이브러리 
'''
- bisect_left(a, x)
    - 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스 반환 

- bisect_right(a, x) 
    - 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스 반환 
'''
from bisect import bisect_right, bisect_left

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    print(right_index)
    left_index = bisect_left(a, left_value)
    print(left_index)
    return right_index - left_index

a = list(map(int, input().split()))

print(count_by_range(a, 4, 4))

print(count_by_range(a, -1, 3))
