def win_rate(score: str, i, weights):
    w, l = 0, 0
    n_heavier = 0

    for j in range(len(score)):
        if score[j] == 'N':
            continue
        elif score[j] == 'W':
            w += 1
            if weights[i] < weights[j]:
                n_heavier += 1
        else:
            l += 1
    n = w + l
    if n == 0:
        return (0, n_heavier)
    else:
        return (w / n, n_heavier)


def solution(weights, head2head):
    infos = []
    for i in range(len(weights)):
        rate, n_heavier = win_rate(head2head[i], i, weights)
        info = (-rate, -n_heavier, -weights[i], i)
        infos.append(info)
    infos.sort()

    answer = [info[3] + 1 for info in infos]
    return answer


"""
우선순위: (-승률, -몸무게 무거운 복서 이긴 횟수, -자기 몸무게, +번호)
"""