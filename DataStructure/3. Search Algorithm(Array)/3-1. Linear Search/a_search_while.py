def seq_search(x, key):
    i = 0

    while True :
        if i == len(x):
            return -1 

        if x[i] == key :
            return i

        i += 1


num = int(input("Input Elements : "))

data = [None] * num 

for i in range(num):
    data[i] = int(input(f"data[{i}] : "))

key = int(input("Input Search Key : "))

result = seq_search(data, key)

if result == -1 :
    print("Not search")
else :
    print(f"x[{result}]")