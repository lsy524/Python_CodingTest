# 순열 
# (A, B) != (B, A) 
from itertools import permutations

data = ["A", "B", "C"]

result = list(permutations(data, 3)) # 모든 순열 구하기 

print(result) # [("A", "B", "C"), ("A", "C", "B"), ("B", "A", "C"), ("B", "C", "A"), ("C", "A", "B"), ("C", "B", "A")]

print(len(result)) # 6
