# 반복적으로 구현한 n! 
def factorial_iteratvie(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱함 
    for i in range(1, n+1):
        result *= i 
    return result 

# 재귀적으로 구현한 n! 
def factorial_recursive(n):
    if n <= 1 : # n이 1 이하인 경우 1를 반환
        return 1
    # n! = n * (n - 1)! 
    return n * factorial_recursive(n - 1) 

print("반복적으로 구현 : ", factorial_iteratvie(5))
print("재귀적으로 구현 : ", factorial_recursive(5))