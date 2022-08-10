# 하노이 탑 구현 

# no = 옮겨야 할 원반의 개수, x = 시작 기둥 번호, y = 목표 기둥 번호 
# 원반 no개를 x기둥에서 y기둥으로 옮김
def move(no, x, y) : 
    if no > 1 :
        move(no - 1, x, 6 - x - y) # 6-x-y 는 중간 기둥을 으미ㅣ
    
    print(f"원반 [{no}] = {x}기둥 -> {y}기둥으로 옮김")

    if no > 1 :
        move(no - 1, 6 - x - y, y)

# x = int(input())
move(3, 1, 3)