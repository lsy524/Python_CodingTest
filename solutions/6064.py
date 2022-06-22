import math
from re import L

x, y, z = map(int, input().split())

if x > y :
    if y > z :
        print(z)
    else :
        print(y)
elif x > z :
    print(z)
else :
    print(x)