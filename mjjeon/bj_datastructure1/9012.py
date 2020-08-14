import sys

cnt = int(sys.stdin.readline().rstrip())
while_cnt = 0

while while_cnt < cnt:

    braces = sys.stdin.readline().rstrip()

    # 열렸다 닫히는 것
    left_cnt = 0
    right_cnt = 0
    braces_cnt = 0
    # 전체 개수
    left_total = 0
    right_total = 0
    # 글자 개수
    char_len = 0
    char_cnt = len(braces)

    while char_len < char_cnt:
        if braces[char_len] == '(':
            left_cnt += 1
            braces_cnt += 1
            left_total += 1
        elif braces[char_len] == ')':
            if braces_cnt > 0 and left_cnt > right_cnt and left_cnt >= right_cnt + 1:
                right_cnt += 1
                braces_cnt -= 1
            right_total += 1

        char_len += 1
    
    if braces_cnt == 0 and left_cnt == right_cnt and left_total == right_total:
        print("YES")
    else:
        print("NO")

    while_cnt += 1