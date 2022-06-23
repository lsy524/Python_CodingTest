n = int(input())

k = list(map(int, input().split()))

# 반복문을 이용한 방법 
result = 999

for i in range(n):
    if result > k[i]:
        result = k[i]

print(result)

# min 함수를 이용한 방법
total = min(k)

print(total)
