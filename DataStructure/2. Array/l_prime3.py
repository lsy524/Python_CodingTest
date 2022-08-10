cnt = 0                         # 곱셈과 나눗셈을 합한 횟수 
ptr = 0                         # 이미 찾은 소수의 개수 
prime = [None] * 500            # 소수를 저장하는 배열 

prime[ptr] = 2
ptr += 1 # 1

prime[ptr] = 3
ptr += 1 # 2 

for n in range(5, 1001, 2) :    # 홀수 만을 대상으로 선정
    i = 1
    while prime[i] * prime[i] <= n :
        cnt += 2

        if n % prime[i] == 0 :  # 나누어 떨어지므로 소수가 아님 
            break               # 반복 중단
        
        i += 1
    
    else :
        prime[ptr] = n
        ptr += 1
        cnt += 1

for i in range(ptr):
    print(prime[i])

print(cnt)


