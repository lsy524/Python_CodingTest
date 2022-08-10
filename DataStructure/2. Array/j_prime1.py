cnt = 0

for i in range(2, 1001):
    
    for j in range(2, i):
        cnt += 1

        if i % j == 0 : break 

    else :
        print(i)
print(cnt)