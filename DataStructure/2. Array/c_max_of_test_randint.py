# 배열 원소의 최댓값을 구해서 출력(원솟값을 난수로 생성 및 max 파일에서 max_of 함수 가져옴)

import random
from a_max import max_of 


num = int(input("radom elements : "))
lo = int(input("low : "))
hi = int(input("high : "))
# x = [] # 방법 1
x = [None] * num # 방법 2

for i in range(num):
    # x.append(random.randint(lo, hi)) # 방법 1
    x[i] = random.randint(lo, hi) # 방법 2
    

print(f'x : {x}')
print(f'max_of : {max_of(x)}')

