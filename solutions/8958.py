import sys 

x = int(sys.stdin.readline())


for i in range(x):
    ox_list = list(sys.stdin.readline())
    cnt = 0
    score = 0
    
    for j in ox_list:
        if j == "O":
            cnt += 1
            score += cnt 
        else :
            cnt = 0
    print(score)