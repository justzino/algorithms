import sys

string = sys.stdin.readline().rstrip()
ans = ""
temp = ""
tag = False

for char in string:  # 끝에 split()이 안 붙어서 한 줄 통채로 읽음.

    if char == '<':  # 태그 시작하기.
        tag = True
        ans += temp[::-1] + "<"
        temp = ''

    elif char == '>':  # 태그 끝 부분
        tag = False
        ans += ">"

    elif char == ' ':  # 태그의 안과 밖을 기준으로 다르게 인식.
        if tag:
            ans += ' '
        else:
            ans += temp[::-1] + ' '
            temp = ''
    else:
        if tag:
            ans += char
        else:
            temp += char

ans += temp[::-1]
print(ans)
