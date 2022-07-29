x = int(input())

if x < 0 and x % 2 == 0 :
    print("A")
elif x < 0 and x % 2 != 0 :
    print("B")
elif x > 0 and x % 2 == 0 :
    print("C")
else:
    print("D")