def recur(n):
    if n > 0 :
        recur(n - 1)
        print(n)
        recur(n - 2)

# x = int(input())

recur(4)

