# 조합 
# (A, B) == (B, A) : combinations와 동일
# (A, A), (B, B), (C, C) : combinations와 다른점

from itertools import combinations_with_replacement

data = ["A", "B", "C"]

result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기 (중복 허용 )

print(result) # [("A", "A"), ("A", "B"), ("A", "C"), ("B", "B"), ("B", "C"), ("C", "C")-]
print(len(result))