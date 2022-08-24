# 7 5 9 0 3 1 6 2 4 8
array = list(map(int, input().split()))

for i in range(1, len(array)):
    # 현재 데이터에서 하위에 있는 데이터를 검사하기 때문에
    # 인덱스 i부터 1까지 1씩 감소하며 반복 
    for j in range(i, 0, -1):
        # 현재 데이터에서 바로 앞에 있는 데이터와 비교 연산 
        if array[j] < array[j - 1]: 
            array[j], array[j - 1] = array[j - 1], array[j] # 한 칸씨기 왼쪽으로 이동 
        # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤 
        else :
            break 

print(array)