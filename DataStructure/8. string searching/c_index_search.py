str = "EEEABCEEEABC"
pattern = "ABC"

# index
# 여러개가 포함되면 가장 작은 인덱스 반환, 없으면 ValueError를 내보냄
sindex = str.index(pattern)

# rindex
# 여러개가 포함되면 가장 큰 인덱스 반환, 없으면 ValueError를 내보냄
srindex = str.rindex(pattern)

print(f"index  = {sindex}")
print(f"rindex = {srindex}")