# x에서 key와 일치하는 원소를 이진 검색 

def bin_search(x, key) :
    pl = 0                          # 검색 범위 맨 앞 원소의 인덱스 
    pr = len(x) - 1                 # 검색 범위 맨 끝 원소의 인덱스 

    while True :
        pc = (pl + pr) // 2         # 중아 원소의 인덱스 
        if x[pc] == key :
            return pc               # 검색 성공 
        elif data[pc] < key :
            pr = pc + 1             # 검색 범위를 뒤쪽 절반으로 좁힘  
        else :
            pl = pc - 1             # 검색 범위를 앞쪽 절반으로 좁힘 
        
        if pl > pr :
            break   
    return -1                       # 검색 실패 


num = int(input("Elements : "))
data = [None] * num                 # 원소수가 num인 배열을 생성 

data[0] = int(input("data[0] : "))

for i in range(1, num):
    while True :
        data[i] = int(input(f"data[{i}] : "))
        if data[i] >= data[i - 1]:  # 바로 직전에 입력한 원소 값보다 큰 값을 입력 
            break 

ky = int(input("Key : "))           # 검색할 키값 ky를 입력

result = bin_search(data, ky)       # ky값과 같은 원소를 data에서 검색 

if result == -1:            
    print("X")
else :
    print(f"data[{result}]")
