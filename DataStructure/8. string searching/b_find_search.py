str = "EEEABCEEEABC"
pattern = "ABC"

# find, rfind 둘다 start, end 생략 가능 
# 기본값은 0 ~ len(str)

# find
# 여러개가 포함되면 가장 작은 인덱스 반환, 없으면 -1 반환
sfind = str.find(pattern) 

# rfind
# 여러개가 포함되면 가장 큰 인덱스 반환, 없으면 -1 반환
srfind = str.rfind(pattern) 

print(f"find  = {sfind}")
print(f"rfind = {srfind}")


# index
# 여러개가 포함되면 가장 작은 인덱스 반환, 없으면 ValueError를 내보냄
sindex = str.index(pattern)

# rindex
# 여러개가 포함되면 가장 큰 인덱스 반환, 없으면 ValueError를 내보냄
srindex = str.rindex(pattern)

print(f"index  = {sindex}")
print(f"rindex = {srindex}")