import sys 

a = int(input(""))
b = int(input(""))

# 내가 푼 풀이 
'''
cnt = 0 
for i in range(a):
    print("*", end="")
    cnt += 1
    if cnt % b == 0:
        print()
'''

# solution 
for i in range(a):      # n번 반복 
    print("*", end="")  # 별 찍기 
    if i % b == b - 1 : # n 번 판단 
        print()         # 줄 바꿈 

if a % b :              # 1번 판단 
    print()             # 줄바꿈
