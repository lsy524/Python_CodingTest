#1부터 n까지 정수의 합

# 방법 1. for 문 활용  
def sum_1ton(x):
    result = 0

    for i in range(1, x+1):
        result += i 
    return result 

# 방법 1. while문 활용  
def sum_2ton(x):
    result = 0

    while x > 0:
        result += x
        x -= 1 
    return result

num = int(input())
print(f"for : {sum_1ton(num)}")
print(f"While : {sum_2ton(num)}")