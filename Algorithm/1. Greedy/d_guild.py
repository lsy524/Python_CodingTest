# 모험가 길드 

'''
* 문제 해결 아이디어 
    1. 오름차순 정렬 이후에 공포도가 낮은 모험가부터 하나씩 확인 
    2. 공포를 확인하며 현재 그룹에 포함된 모험가의 수가 현재 확인하고 있는 공포도보다 크거나 같다면 이를 그룹으로 설정 
    
'''

x = int(input())

data = list(map(int, input().split()))

data.sort()

result = 0          # 총 그룹의 수 
cnt = 0             # 현재 그룹에 포함된 모험가의 수 

# 공포도를 낮은 것부터 하나씩 확인하며 
for i in data:      
    cnt += 1        # 현재 그룹에 해당 모험가를 포함시키기
    # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성 
    if cnt >= i :   
        result += 1 # 총 그룹의 수 증가시키기 
        cnt = 0     # 현재 그룹에 포함된 모험가의 수 초기화 

print(result)