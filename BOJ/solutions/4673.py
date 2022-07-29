def selfnum(x):
    x = x + sum(map(int, str(x)))
    return x 

nonselfnum = []

for i in range(1, 10001) :
    nonselfnum.append(selfnum(i))
    
for j in range(1, 10001):
    if j not in nonselfnum:
        print(j)