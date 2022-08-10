import random

n = int(input())

for _ in range(n):
    r = random.randint(10, 20)
    print(r, end=" ")

    if r == 13 :
        print("\nCancle")
        break
else :
    print("\n=====")