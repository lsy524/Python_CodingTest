# 큰수의 법칙 
'''
* 문제 아이디어 
    1. 입력 받은 데이터에서 가장 큰수와 두 번째로 큰 수를 구한다 .
    2. 가장 큰 수를 k 번 더하고, 두 번째로 큰 수를 한번 더한다. 
    3. 더할 때마다 m 값에 -1을 한다.
    4. m값이 0이 되면 종료한다. 
'''

n, m, k = map(int, input().split())    # n, m, k를 공백으로 구분하여 입력

data = list(map(int, input().split())) # n개의 수를 공백으로 구분하여 입력 

data.sort() # 입력받은 수들 정렬 
max_one = data[n - 1] # 가장 큰수 
max_two = data[n - 2] # 두번째로 큰수 

result = 0

while True :
    # k번 반복 
    for i in range(k):
        # m이 0이라면 반복문 탈출 
        if m == 0 :
            break 
        # 가장 큰수를 k번 더함 
        result += max_one
        # 더할 때마다 1씩 감소 
        m -= 1
    # m이 0이라면 반복문 탈출 
    if m == 0 :
        break 
    # 두 번째로 큰 수를 한번 더함 
    result += max_two
    # 더할 때마다 1씩 빼기 
    m -= 1

print(result)

