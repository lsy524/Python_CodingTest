def bubble_sort(data):
    n = len(data)
    k = 0

    while k < n - 1:
        last = n - 1
        for i in range(n - 1, k, -1):
            if data[i - 1] > data[i]:
                data[i - 1], data[i] = data[i], data[i - 1]
                last = i
        k = last 


x = int(input())
data = [None] * x

for i in range(x):
    data[i] = int(input(f"data[{i}] : "))

bubble_sort(data)

print("=======================")

for i in range(x):
    print(f"data[{i}] = {data[i]}")
