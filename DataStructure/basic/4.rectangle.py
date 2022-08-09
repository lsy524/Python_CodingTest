# 약수 구하는 프로그램 
a = int(input())


for i in range(1, a + 1):
    if i * i > a : break 
    if a % i : continue 
    print(f'{i} x {a // i}')
