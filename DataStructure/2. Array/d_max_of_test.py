# 긱 배열(튜플, 문자열, 문자열 리스트) 원소의 최댓값 출력

from a_max import max_of 

t = (4,7,5.6,2,3.14,1)
s = 'string'
a = ["DTS", "AAC", "FLAC"]

print(f'{t} max_of : {max_of(t)}')
print(f'{t} max : {max(t)}')
print("===========================")
print(f'{s} max_of : {max_of(s)}')
print(f'{s} max : {max(s)}')
print("===========================")
print(f'{a} max_of : {max_of(a)}')
print(f'{a} max : {max(a)}')
print("===========================")