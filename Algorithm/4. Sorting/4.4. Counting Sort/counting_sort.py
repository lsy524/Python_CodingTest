# 모든 원소의 값이 0보다 크거나 같다고 가정 
array = list(map(int, input().split()))

count = [0] * (max(array) + 1) # 모든 범위를 포함하는 리스트 선언(모든 값을 0으로 초기화)

for i in range(len(array)):
    count[array[i]] += 1       # 각 데이터에 해당하는 인덱스의 값 증가  

# 리스트에 기록된 정렬 정보 확인 
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end= " ")      # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력