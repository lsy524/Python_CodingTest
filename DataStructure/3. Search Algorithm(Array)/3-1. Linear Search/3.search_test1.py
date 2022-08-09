from search import seq_search

x = []
num = 0

while True :
    s = input(f"x[{num}] : ")
    if s == "End" : break 
    x.append(float(s))
    num += 1


key = float(input("Input Search Key : "))

result = seq_search(x, key)

if result == -1 :
    print("Not Search")
else :
    print(f"x[{result}]")
