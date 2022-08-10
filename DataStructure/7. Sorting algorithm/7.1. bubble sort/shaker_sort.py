

def shaker_sort(data):
    left = 0
    right = len(data) - 1
    last = right
    
    while left < right :
        for i in range(right, left, -1) :
            if data[i - 1] > data[i] :
                data[i - 1], data[i] = data[i], data[i - 1]
            last = i 
        left = last 

        for j in range(left, right):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                last = j
        right = last 

x = int(input())
data = [None] * x

for i in range(x):
    data[i] = int(input(f"data[{i}] : "))

shaker_sort(data)

print("=======================")

for i in range(x):
    print(f"data[{i}] = {data[i]}")