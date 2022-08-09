cnt = 0 # 나눗셈 횟수 
ptr = 0 # 이미 찾은 소수의 개수 
prime = [None] * 500 # 소수를 저장하는 배열 

prime[ptr] = 2 # 2는 소수이므로 초기값 지정  
ptr += 1 

for n in range(3, 1001, 2): # 홀수만을 대상으로 선정 
    for i in range(1, ptr): # 이미 찾은 소수로 나눔 
        cnt += 1
        if n % prime[i] == 0 : # 나누어 떨어지면 소수가 아님  
            break  # 반복 중단 
    else :
        prime[ptr] = n # 소수로 배열 등록 
        ptr += 1

for i in range(ptr):
    print(prime[i])

print(cnt)