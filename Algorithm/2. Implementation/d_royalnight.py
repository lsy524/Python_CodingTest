# 왕실 나이트 

'''
* 문제 해결 아이디어 
    - 나이트가 움직일 수 있는 경로를 변수에 넣는다 
        - 1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동 
        - 2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동 
    - 나이트의 현재 위치가 주어지면 현재 위치에서 이동 경로를 더한 다음, 8 x 8 좌표 평면에 있는지 확인하면 됨 
    - 위의 과정을 반복문으로 처리하면 됨 
'''

data_input = input()    # 현재 나이트의 위치 입력 

row = int(data_input[1]) # 나이트 위치의 행을 row 변수에 할당 

column = int(ord(data_input[0])) - int(ord("a")) + 1 # 나이트의 열을 column에 할당 

# 나이트가 이동할 수 있는 8가지 방향 정의 
steps = [(1, -2), (1, 2), (2, -1), (2, 1), (-2, -1), (-2, 1), (-1, 2),(-1, 2)]

result = 0

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인 
for step in steps :
    
    # 이동하고자 하는 위치 확인 
    next_row = row + step[0]
    next_column = column + step[1]

    # 해당 위치로 이동이 가능하다면 카운트 증가 
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)