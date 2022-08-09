def seq_search(data, key):
    for i in range(len(data)):
        if data[i] == key :
            return i 
    return -1 

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