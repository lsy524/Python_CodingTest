# 조합
# (A, B) == (B, A)

from itertools import combinations


data = ["A", "B", "C"]

# 중복은 제거한 조합 출력 

result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기 

print(result) # [("A", "B"), ("A", "C"), ("B", "C")]
print(len(result))  # 3