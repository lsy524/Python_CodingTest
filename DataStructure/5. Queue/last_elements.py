# 링 버퍼 활용 
# 오래된 데이터를 버리는 프로그램

# 원하는 개수(n)만큼 값을 입력받아 마지막 n개를 저장 

n = int(input("elements count : "))
a = [None] * n 

cnt = 0

while True :
    a[cnt % n] = int(input(f"{cnt+1} : "))
    cnt +=1 

    retry = input("retry : ")
    if retry in {'N', "n"} :
        break 

i = cnt - n 
if i < 0 : i = 0

while i < cnt :
    print(f"{i + 1} = {a[i % n]}")
    i += 1 