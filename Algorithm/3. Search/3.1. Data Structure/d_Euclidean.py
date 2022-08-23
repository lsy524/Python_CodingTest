def gcd(a, b):
    # a가 b에 배수라면 b를 반환 
    if a % b == 0:
        return b 
    
    else :
        return gcd(b, a % b)


print(gcd(192, 162))