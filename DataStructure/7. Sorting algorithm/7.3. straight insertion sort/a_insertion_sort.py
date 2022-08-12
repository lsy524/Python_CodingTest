# 단순 삽입 정렬 알고리즘 구현 

def insertion_sort(a):
    n = len(a)

    for i in range(1, n):   
        j = i               # j변수에 현재 인덱스 대입 
        tmp = a[i]          # tmp에 현재 정렬을 반복할 원소를 대입
        
        # j(현재 인덱스)가 0 보다 크고 a[j - 1](현재 인덱스보다 앞 인덱스)가 tmp(현재 값)보다 큰 경우 반복문 실행  
        while j > 0 and a[j - 1] > tmp :
            a[j] = a[j - 1] # a[j](현재 인덱스)에 a[j-1](현재 인덱스보다 앞 인덱스) 값을 대입 
            j -= 1          
        a[j] = tmp          # 현재 인덱스에 tmp(현재 원소)를 대입 


num = int(input("elements : "))
x = [None] * num 

for i in range(num):
    x[i] = int(input(f"x[{i}] : "))

insertion_sort(x)

for i in range(len(x)):
    print(f"x[{i}] = {x[i]}")