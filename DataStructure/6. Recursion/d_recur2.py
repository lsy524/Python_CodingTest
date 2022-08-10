def recur(x):
    if x > 0 :
        recur(x - 2)
        print(x)
        recur(x - 1)

x = int(input())
recur(x)