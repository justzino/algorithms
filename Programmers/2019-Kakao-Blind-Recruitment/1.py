def solution(N, stages):
    # stage, 실패, 누적도전자, 실패율
    level = [[i, 0, 0, 0] for i in range(N + 2)]
    n_people = len(stages)

    for i in stages:
        level[i][1] += 1

    level[1][2] = n_people
    level[1][3] = level[1][1] / n_people
    for i in range(2, N + 2):
        level[i][2] = level[i - 1][2] - level[i - 1][1]
        try:
            level[i][3] = level[i][1] / level[i][2]
        except ZeroDivisionError:
            level[i][3] = 0

    level = level[1:-1]
    level.sort(key=lambda x: x[3], reverse=True)
    answer = [x[0] for x in level]

    return answer
