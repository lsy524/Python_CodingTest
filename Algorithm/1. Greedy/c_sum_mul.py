# 곱하기 혹은 더하기 
'''
* 문제 해결 아이디어 
    - 곱하기를 많이 하여 값을 크게 만든다
    - 단, 두 수 중에서 하나라도 0 혹은 1인 경우 곱하기보다는 더하기를 수행
    - 즉, 두 수 중에서 하나라도 1이하인 경우네는 더하며, 두 수가 모두 2 이상인 경우에는 곱하기 
'''

# 직접 푼 풀이  
x = input()

result = int(x[0])  # 첫번째 문자를 숫자로 변경하여 대입

for i in range(1, len(x)):
    n = int(x[i])
    # 두 수가 모두 2이상이라면 곱하기를 수행  
    if n >= 2 and result >= 2:
        result *= n
    # 아니면 더하기를 수행 
    else :
        result += n
    
print(result)

#======================================================================

# 답안 예시 
data = input()
result2 = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    # 두 수 중에서 하나라도 0 혹은 1 인 경우, 곱하기보다는 더하기 수행 
    if num <= 1 or result2 <= 1 :
        result2 += num 
    else :
        result2 *= num

print(result2)


