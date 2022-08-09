# 리스트 원소와 복사 

# 1. 자료형을 정하지 않은 리스트의 원소 확인 
x = [15, 64, 7, 3.14, [32,55], "ABC"]

for i in range(len(x)):
    print(f"x[{i}] = {x[i]}")

# 2. 리스트 얕은 복사 copy() 
lst1 = [[1,2,3], [4,5,6]]
lst2 = lst1.copy()

lst1[0][1] = 9

# lst1의 원소를 9로 바꿨지만 lst2까지 함께 변경됨
print(lst1) 
print(lst2)

# 3. 리스트 깊은 복사 deepcopy()
import copy
lst3 = [[1,2,3], [4,5,6]]
lst4 = copy.deepcopy(lst3)

lst3[0][2] = 88

print(lst3)
print(lst4)