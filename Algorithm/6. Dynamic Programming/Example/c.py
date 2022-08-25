# 효율적인 화폐 구성 
'''
* 문제 해결 아이디어 
    - ai = 금액 i를 만들 수 있는 최소한의 화폐 개수 
    - k = 각 화폐의 단위 
    - 점화식 : 각 화페 단위인 k를 하나씩 확인하며
        - ai-k를 만드는 방법이 존재하는 경우 => ai = min(ai, ai-k+1)
        - ai-k를 만드는 방법이 존재하지 않는 경우 => ai = INF
'''

n, m = map(int, input().split())

# n개의 화폐 단위 정보를 입력 받음 
array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1) # 한번 계산된 결과를 저장하기 위한 dp 테이블 초기화 

d[0] = 0 # 첫번째 화폐 설정 

# 다이나믹 프로그래밍 진행(보텀업)
# i = 화폐 단위 
for i in range(n):
    # j = 금액 
    for j in range(array[i], m + 1):
        # (i - k)원을 만드는 방법이 존재하는 경우 
        if d[j - array[i]] != 10001 : 
            d[j] = min(d[j], d[j - array[i]] + 1)

# m원을 만드는 방법이 존재하지 않는 경우 
if d[m] == 10001 :
    print(-1)
# m원을 만드는 방법이 존재하는 경우 
else :
    print(d[m])