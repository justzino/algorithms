INF = 101


def solution(progresses, speeds):
    remains = [100 - progress for progress in progresses]

    days_required = []
    for i in range(len(speeds)):
        q, r = divmod(remains[i], speeds[i])
        if r > 0:
            q += 1
        days_required.append(q)

    answer = []
    stack = []

    for day in days_required:
        if not stack or stack[0] >= day:
            stack.append(day)
        else:
            answer.append(len(stack))
            stack = [day]
    answer.append(len(stack))

    return answer
