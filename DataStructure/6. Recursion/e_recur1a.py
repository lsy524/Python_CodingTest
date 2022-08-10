# 비재귀적으로 재귀 함수 구현(꼬리 재귀 제거)

def recur(x):
    while x > 0 :
        recur(x - 1)
        print(x)
        # recur(x - 2) 꼬리 재귀  
        x = x - 2 


x = int(input())
recur(x)