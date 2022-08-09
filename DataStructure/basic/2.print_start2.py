a = int(input())
b = int(input())

for _ in range(a // b):
    print(b * "*")

rest = a % b 
if rest :
    print("*" * rest)