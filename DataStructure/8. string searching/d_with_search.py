# 어떤 문자열이 다른 문자열의 시작이나 끝에 포함되어 있는지 판단

str = "EEEABCEEEABC"
pattern = "ABC"

# 문자열이 prefix로 시작하면 True, 그렇지 않으면 False
# startsWith(prefix로, start, end) -> start, end 생략 가능 
startswith = str.startswith(pattern) # False

# 문자열이 suffix 끝나면 True, 그렇지 않으면 False
# endsWith(suffix, start, end) -> start, end 생략 가능 
endswith = str.endswith(pattern) # True

print(f"startsWith = {startswith}")
print(f"endswith   = {endswith}")
