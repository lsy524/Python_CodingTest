data = ["ManUTD", "RealMadrid", "Chelsea", "Tottenham"]

# 방법 1. 리스트의 모든 원소를 스캔하기(원소 수를 미리 파악)
for i in range(len(data)):
    print(f'x[{i}] = {data[i]}')
print()

# 방법 2. enumerate() 함수 
for i, name in enumerate(data) :
    print(f'x[{i}] = {name}')
print()

# 방법 3. enumerate 함수 : 1부터 카운트 
for i, name in enumerate(data, 1):
    print(f'{i}번째 = {name}')
print()

# 방법 4. 인덱스 값 사용하지 않고 스캔 
for i in data:
    print(i)