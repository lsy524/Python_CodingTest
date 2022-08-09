# 매번 if..continue를 사용하기 때문에 비효율적 

for i in range(1, 13):
    if i == 8 : continue
    print(i, end=" ")