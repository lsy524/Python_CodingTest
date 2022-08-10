def recur(x):
    while x > 0 :
        recur(x - 1)
        print(x)
        x = x - 2 


x = int(input())
recur(x)