def bin_search(x, key) :
    pl = 0
    pr = len(x) - 1

    while True :
        pc = (pl + pr) // 2 
        if x[pc] == key :
            return pc 
        elif data[pc] > key :
            pl = pc + 1
        else :
            pr = pc - 1 
        
        if pl > pr :
            break 
    return -1 


num = int(input("Elements : "))
data = [None] * num 

data[0] = int(input("data[0] : "))

for i in range(1, num):
    while True :
        data[i] = int(input(f"data[{i}] : "))
        if data[i] >= data[i - 1]:
            break 

ky = int(input("Key : "))

result = bin_search(data, ky)

if result == -1:
    print("X")
else :
    print(f"data[{result}]")
