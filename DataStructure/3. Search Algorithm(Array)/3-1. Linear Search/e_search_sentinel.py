import copy 

def seq_search(data, key) :
    x = copy.deepcopy(data)
    x.append(key)

    i = 0

    while True :
        if x[i] == key :
            break 
        i += 1
    
    return -1 if i == len(data) else i



num = int(input("Input num : "))
data = [None] * num 

for i in range(num):
    data[i] = int(input(f"data[{i}] : "))

key = int(input("Input key : "))

result = seq_search(data, key)

if result == -1 :
    print("X")
else :
    print(f"data[{result}]")