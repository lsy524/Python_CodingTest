# 10진수 정숫값을 입력받아 2 ~ 36 진수로 변환 
def card_conv(x, y):
    d = ""
    dchar = '0123456789ABCDEFGHUJKLMNOPQRSTUVWXYZ'

    while x > 0 :
        d += dchar[x % y]
        x //= y
    
    return d[::-1]

while True:
    while True :
        num = int(input("변환할 정수 입력 : "))
        if num > 0: break 
    
    while True :
        x = int(input("진수 입력 : "))
        if x > 0 : break 

    print(f"{x}진수로 {card_conv(num, x)}")

    retry = int(input("Retry : "))
    if retry in {"n", "N"}: break