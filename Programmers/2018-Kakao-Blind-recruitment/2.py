import re


def solution(dartResult):
    bonus = {'S': 1, 'D': 2, 'T': 3}
    pattern = re.compile('([0-9]+)([SDT])([*#]?)')
    score_list = pattern.findall(dartResult)

    result = []
    for score in score_list:
        result.append(int(score[0]))
        result[-1] = result[-1] ** bonus[score[1]]

        if score[2] == '*':
            try:
                result[-1] = result[-1] * 2
                result[-2] = result[-2] * 2
            except:
                continue
        elif score[2] == '#':
            result[-1] = result[-1] * (-1)

    answer = sum(result)
    return answer
