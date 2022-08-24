# 이잔탐색 재귀적 구현 

def binary_search(array, start, end, target):

    if start > end :
        return None 
    
    mid = (start + end) // 2    # 중간점 설정 

    # 찾은 경우 
    if array[mid] == target :
        return mid  # 중간점 값 인덱스 반환
    
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 
    elif array[mid] > target :
        return binary_search(array, start, mid - 1, target) # 끝 값을 중간점 - 1 값으로 설정 
    
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 
    else :
        return binary_search(array, mid + 1, end, target) # 시작 값을 중간점 + 1 값으로 설정 

n, target = map(int, input().split())   # 원소 개수(n), 찾고자 하는 값(target) 입력 

array = list(map(int, input().split())) # 전체 원소 입력 

result = binary_search(array, 0, n - 1, target) # 이진 탐색 수행 

# 결과 출력 
if result == None :
    print("원소가 존재하지 않음")
else :
    print(result + 1)