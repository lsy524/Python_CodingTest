# 양의 정수 팩토리얼 함수 구현 
def factorial(x):
    if x > 0 :
        return x * factorial(x - 1)
    else :
        return 1 

a = int(input("factorial func : "))

a_result = factorial(a)

print(a_result)

# math 라이브러리 factorial 활용 
import math 

b = int(input("math.factorial : "))

b_result = math.factorial(b)

print(b_result)