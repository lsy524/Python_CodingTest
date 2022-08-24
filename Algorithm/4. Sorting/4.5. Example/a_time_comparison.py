# 선택 정렬과 기본 정렬 라이브러리 수행 시간 비교 
'''
선택 정렬 측정 시간 : 5.823998689651489
기본 정렬 라이브러리 측정 시간 : 0.0020084381103515625

기본 정렬 라이브러리가 선택 정렬 보다 훨씬 짧은 시간에 정렬을 수행 
'''

from random import randint
import time 

array1 = []

# 10,000번 반복
for _ in range(10000):
    array1.append(randint(1, 100)) # 배열에 1부터 100 사이의 랜덤한 정수 삽입

start_time_1 = time.time()  # 선택 정렬 프로그램 성능 측정 

# 선택 정렬 프로그램 성능 측정 
for i in range(len(array1)):
    min_index = i 
    for j in range(i + 1, len(array1)) :
        if array1[min_index] > array1[j]:
            min_index = j 
    array1[i], array1[min_index] = array1[min_index], array1[i]


end_time_1 = time.time()    # 선택 정렬 프로그램 측정 종료 

print(f"선택 정렬 성능 측정 : {end_time_1 - start_time_1}") # 수행 시간 출력


array2 = []

# 10,000번 반복
for _ in range(10000):
    array2.append(randint(1, 100))# 배열에 1부터 100 사이의 랜덤한 정수 삽입

start_time_2 = time.time()  # 기본 정렬 라이브러리 성능 측정 

array2.sort()   # 기본 정렬 라이브러리 사용 

end_time_2 = time.time()    # 기본 정렬 라이브러리 측정 종료 

print(f"기본 정렬 라이브러리 정렬 성능 측정 : {end_time_2 - start_time_2}") # 수행 시간 출력 

