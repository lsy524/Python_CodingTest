# 리스트에서 임의의 원솟값을 업데이트 

def change(lst, idx, val): # list index value를 매개변수로 받음 
    lst[idx] = val 


x = [11,22,33,44,55,66]
print("x =", x)

index = int(input("Inpt Update Index : "))
value = int(input("Inuput Update Value : "))

change(x, index, value)
print("x =", x)