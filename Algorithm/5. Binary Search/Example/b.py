# 정렬된 배열에서 특정 수의 개수 구하기 

from bisect import bisect_left, bisect_right

# 값이 [right_value, left_value]인 데이터의 개수를 반환하는 함수 
def count(array, right_value ,left_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)

    return  right_index - left_index


n, m = list(map(int, input().split())) # 데이터의 개수 n, 찾고자 하는 값 x 입력받기 

array = list(map(int, input().split())) # 전체 데이터 입력 받기 

# 값이 [m, m] 범위에 있는 데이터의 개수 계산 
cnt = count(array, m, m)

# 값이 m인 원소가 존재하지 않는다면 
if cnt == 0 : 
    print(-1)   # -1 반한
# 값이 m인 원소가 존재한다면 
else : 
    print(cnt) # cnt 값 반환 
