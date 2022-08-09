# 순열 + 조합 
# (A, B) != (B, A) : permutaions와 동일 
# (A, A), (B, B) : combinations_with_placement와 동일 

from itertools import product

data = ["A", "B", "C"]

result = list(product(data, repeat = 2)) # 2개를 뽑는 모든 순열 구하기(중복 허용)

print(result) #[("A", "A"), ("A", "B"), ("A", "C"), ("B", "A"), ("B", "B"), ("B", "C"), ("C", "A"), ("C", "B"), ("C", "C")]
print(len(result)) # 9