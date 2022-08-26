# 금광 문제 

'''
* 문제 해결 아이디어 
    - 금광의 모든 위치에 대하여 다음의 세 가지만 고려하면 됨
        1. 왼쪽 위에서 오는 경우
        2. 왼쪽 아래에서 오는 경우 
        3. 왼쪽에서 오는 경우 

    - 세 가지 경우에서 가장 많은 금을 가지고 있는 경우를 테이블에 갱신주면 됨     
        - array[i][j] = i행, j열에 존재하는 금의 양
        - dp[i][j] = i행, j열까지의 최적의 해(얻을 수 있는 금의 최댓값)
        - 점화식
            - dp[i][j] = array[i][j] + max(dp[i - 1][j - 1], dp[i][j - 1], dp[i + 1][j - 1])
'''

# 테스트 케이스 입력 
for tc in range(int(input())):
    # 금광 정보 입력 
    n, m = map(int, input().split())    
    arr = list(map(int, input().split()))

    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화 
    dp = []
    index = 0
    for i in range(n):
        dp.append(arr[index:index+m])
        index += m

    # 다이나믹 프로그래밍 진행 
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우 
            if i == 0: left_up = 0  # 매 열 마다 첫 번째 행은 위에서 올 수 없기 때문에 인덱스 값을 벚어나는 경우를 대비해 첫 번째 행 일 시 기본 값 설정 
            else : left_up = dp[i - 1][j - 1]
            
            # 왼쪽 아래에서 오는 경우 
            if i == n - 1 : left_down = 0  # 매 열 마다 마지막(n - 1) 행은 아래에서 올 수 없기 때문에 인덱스 값을 벚어나는 경우를 대비해 마지막(n - 1) 행 일 시 기본 값 설정
            else : left_down = dp[i + 1][j - 1]

            # 왼쪽에서 오는 경우 
            left = dp[i][j - 1]

            # 가장 큰 값을 가지는 경우에 현재 값을 더해서 현재 위치에 대한 값을 할당
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    
    result = 0

    for i in range(n):
        result = max(result, dp[i][m - 1])  # 가장 오른쪽 열에 대한 정보 중 가장 큰 값을 result에 할당
    print(result)

