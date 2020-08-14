n = int(input())
string = list(input())  # 문자열 한글자 한글자 저장
s = 0

for i in string:
    s += int(i)

print(s)
