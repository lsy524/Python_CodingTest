def selection_sort(x):
    n = len(x)
    
    for i in range(n - 1):
        min = i 
        for j in range(i + 1, n):
            if x[j] < x[min]:
                min = j 
        x[i], x[min] = x[min], x[i]


x = int(input("elements : "))
data =[None] * x

for i in range(x):
    data[i] = int(input(f"data[{i}] : "))

selection_sort(data)

for i in range(x):
    print(f"data[{i}] = {data[i]}")