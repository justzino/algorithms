import re


def solution(dartResult):
    pattern = re.compile('([0-9]+)([SDT])([*#]?)')
    score_list = pattern.findall(dartResult)
    print(score_list)

    result = []
    for score in score_list:
        result.append(int(score[0]))

        if score[1] == 'S':
            pass
        elif score[1] == 'D':
            result[-1] = result[-1] ** 2
        else:
            result[-1] = result[-1] ** 3

        if score[2] == '*':
            try:
                result[-1] = result[-1] * 2
                result[-2] = result[-2] * 2
            except:
                continue
        elif score[2] == '#':
            result[-1] = result[-1] * (-1)
        else:
            pass

    answer = sum(result)
    return answer