def solution(N, stages):
    level = [0 for _ in range(N + 2)]  # stage 별 실패자
    n_people = [0, len(stages)]  # stage 별 도전자
    rate = {}  # stage: 실패율

    for stage in stages:
        level[stage] += 1

    rate[1] = (level[1] / n_people[1])
    for i in range(2, N + 1):
        n_people.append(n_people[i - 1] - level[i - 1])
        try:
            rate[i] = level[i] / n_people[i]
        except ZeroDivisionError:
            rate[i] = 0

    return sorted(rate, key=lambda x: -rate[x])
