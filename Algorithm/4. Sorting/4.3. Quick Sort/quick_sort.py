array = list(map(int, input().split()))

def quick_sort(array, start, end):
    # 원소가 1개인 경우 종료 
    if start >= end :
        return 
    
    pivot = start       # 피벗은 첫 번째 원소 
    right = end 
    left = start + 1 

    while(left <= right) :

        # 피벗보다 큰 데이터를 찾을 때까지 반복 
        while(left <= end and array[left] <= array[pivot]) :
            left += 1
        
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        
        # 엇갈린 경우 
        if(left > right) :
            array[right], array[pivot] = array[pivot], array[right] # 작은 데이터와 피벗을 교체
        # 엇갈리지 않은 경우 
        else :
            array[left], array[right] = array[right], array[left]   # 작은 데이터와 큰 데이터를 교체
    
    # 분할 이후 왼쪽 부분을 정렬 
    quick_sort(array, start, right - 1)
    # 분할 이후 오른쪽 부분을 정렬
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)