def solution(s):
    n = len(s)
    result = [n, ]

    for gap in range(1, n // 2 + 1):
        last = s[0: gap]    # 직전 문자열 block = 첫 block 초기화
        num = 1
        string = ''
        end_index = n // gap

        for i in range(1, end_index):
            x = gap * i
            now = s[x: x + gap]     # 현재 문자열 block
            # 이전 문자열과 같은 경우
            if now == last:
                num += 1

            # 이전 문자열과 다른 경우
            else:
                if num == 1:
                    string += last
                    last = now
                else:
                    string += str(num) + last
                    num = 1
                    last = now

            # gap 크기를 유지한 마지막 block
            if i == end_index - 1:
                if num == 1:
                    string += now
                else:
                    string += str(num) + now

        # 압축하고 뒤에 남은 부분
        string += s[end_index * gap:]
        result.append(len(string))

    return min(result)


# 테케
# print(solution("a"))    # 1, 5번 히든 테케 - 통과 못함
print(solution("aabbaccc"))     # 7
print(solution("ababcdcdababcdcd"))     # 9
print(solution("abcabcabcabcdededededede"))     # 14
print(solution("xababcdcdababcdcd"))     # 17
