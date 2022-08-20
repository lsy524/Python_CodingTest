# 숫자 카드 게임 
'''
* 문제 풀이 아이디어 
    1. 행 마다 가장 작은 값을 구한다 
        - min 함수 이용 
    2. 그 중에서 가장 큰 값을 구한다.
        - max 
'''

# min 함수 이용 
n1, m1 = map(int, input().split()) # n1, m1을 공백으로 구분하여 입력 
result1 = 0 

# 한 줄씩 입력 받아 확인
for i in range(n1):
    data1 = list(map(int, input().split()))
    min_value1 = min(data1) # 현재 줄에 가장 작은 수 찾기 
    result1 = max(result1, min_value1) # 가장 작은 수 중에서 가장 큰 수 찾기 

print(result1)

#==========================================================================
# 2중 반복문 구조를 이용
n2, m2 = map(int,input().split())

result2 = 0

for i in range(n2) :
    data2 = list(map(int, input().split()))

    min_value2 = 10001 # 초과하는 값으로 초기화 

    # 현재 줄에서 가장 작은 수 찾기 
    for j in data2 :
        min_value2 = min(min_value2, j)
    
    result2 = max(result2, min_value2) # 가장 작은 수 들 중에서 가장 큰 수 찾기

print(result2)
