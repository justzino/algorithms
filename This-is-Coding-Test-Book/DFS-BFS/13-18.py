def reverse(p):
    if not p:
        return ""

    result = ""
    for c in p:
        if c == '(':
            result += ')'
        else:
            result += '('

    return result


def solution(p):
    # 문자열이 비었으면 종료
    if not p:
        return ""

    length = len(p)
    brace_count = 0
    correct = True

    for i in range(length):
        if p[i] == '(':
            brace_count += 1
        else:
            brace_count -= 1

        # 올바른 문자열이 아닌 경우
        if brace_count < 0:
            correct = False

        # 균형잡힌 괄호 문자열이 된 경우
        elif brace_count == 0:
            # 올바른 문자열이면 그대로 return
            if correct:
                return p[:i + 1] + solution(p[i + 1:])
            # 올바르지 않은 문자열이면 알고리즘 수행
            else:
                return '(' + solution(p[i + 1:]) + ')' + reverse(p[1: i])

