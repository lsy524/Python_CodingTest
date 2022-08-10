# 배열 원소의 최댓값을 구해서 출력(원솟값 입력 및 max 파일에서 max_of 함수 import)

from a_max import max_of 

x = []
num = 0 

while True :
    s = input("Input Elements : ")

    if s == "End": break 

    x.append(int(s))
    num += 1


print(f'num : {num}')
print(f'max_of : {max_of(x)}')
