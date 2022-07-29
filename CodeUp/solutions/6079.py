x = int(input())
result = 0


for i in range(x+1):
    result += i 
    if result >= x :
        break
print(i)