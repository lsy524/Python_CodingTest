# 순수한 재귀 함수 역순 출력 구현 

def recur(x):
    if x > 0 :
        recur(x - 2)
        print(x)
        recur(x - 1)

x = int(input())
recur(x)