# 피보나치 함수를 재귀함수로 구현

'''
* 단순 재귀 함수로 피보나치 수열을 해결하면 지수 시간 복잡도를 가지게 됨
''' 

def fibo(x):
    if x == 1 or x == 2:
        return 1
    else : 
        return fibo(x - 1) + fibo(x - 2)

print(fibo(4))