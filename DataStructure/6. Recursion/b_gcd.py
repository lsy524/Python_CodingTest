# 유클리드 호제법으로 최대 공약수를 구하는 gcd 함수 구현 

def gcd(x, y):
    if y == 0:
        return x 
    else :
        return gcd(y, x % y)

x, y = map(int, input().split())

a_result = gcd(x, y)

print(a_result)

# math 라이브러리 gcd 활용 
import math 

a, b = map(int, input().split())

b_result = math.gcd(a, b)
print(b_result)