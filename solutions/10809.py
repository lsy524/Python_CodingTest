# find : 찾는 문자가 문자열 안에서 첫번째에 위치한 순서를 숫자로 출력하고 
#        만일 문자가 없을 경우 -1 을 출력
# chr : 숫자 -> 문자
# ord : 문자 -> 숫자

s = input()
alphabet = list(range(97, 123))

for i in alphabet:
    print(s.find(chr(i)), end=" ")