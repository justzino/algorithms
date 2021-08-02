from collections import deque


def solution(priorities, location):
    nums_sorted = sorted(priorities)
    q = deque([(p, i) for i, p in enumerate(priorities)])

    answer = 1
    while True:
        if q[0][0] < nums_sorted[-1]:
            q.append(q.popleft())
            continue
        nums_sorted.pop()
        now = q.popleft()

        if now[1] == location:
            break
        answer += 1

    return answer
