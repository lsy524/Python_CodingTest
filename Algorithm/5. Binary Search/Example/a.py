# 떡볶이 떡 만들기 
'''
* 문제 해결 아이디어 
    - 적절한 높이를 찾을 때까지 이진 탐색을 수행하여 높이 H를 반복해서 조정 
    - '현재 이 높이로 자르면 조건을 만족할 수 있는가?'를 확인한 뒤에 조건의 만족 여부("예" 혹은 "아니오")에 따라서 탐색 범위를 좁혀서 해결
    - 절단기 높이는 0 ~ 10억까지의 정수 중 하나 
        ***** 이렇게 큰 탐색 범위를 보면 가장 먼저 이진 탐색을 떠올려야함 ***** 
'''


n, m = list(map(int, input().split()))  # 떡의 개수(n)와 요청한 떡의 길이(m) 입력
array = list(map(int, input().split())) # 각 떡의 개별 높이 정보 입력 

start = 0           # 시작점 
end = max(array)    # 끝점 

result = 0 

# 이진 탐색 수행 
while start <= end :
    total = 0
    mid = (start + end) // 2

    for i in array:
        # 잘랐을 때 떡의 양 계산
        if i > mid :
            total += i - mid 
    
    # 떡의 양이 부족한 경우 더 많이 자르기
    if total < m :
        end = mid - 1 # 왼쪽 부분 탐색
    # 떡의 양이 충분한 경우 덜 자르기 
    else :
        result = mid     # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1 # 오른쪽 부분 탐색

print(result)


