# 효율성 통과 못하는 풀이 - me
from collections import deque


def solution(food_times, k):
    n = len(food_times)
    q = deque()

    for i in range(n):
        q.append((i, food_times[i]))

    while q:
        food, time = q.popleft()

        if k == 0:
            return food + 1

        k -= 1
        time -= 1

        if time == 0:
            continue
        q.append([food, time])

    return -1


print(solution([3, 1, 2], 5))
