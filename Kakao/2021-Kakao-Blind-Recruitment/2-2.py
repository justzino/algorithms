from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    result = []
    for i in course:
        course_dict = defaultdict(int)
        for order in orders:
            for c in combinations(order, i):
                c = list(c)
                c.sort()
                x = ''.join(c)
                course_dict[x] += 1
        if not course_dict:
            continue

        max_count = max(course_dict.values())
        if max_count < 2:
            continue

        for k, v in course_dict.items():
            if v == max_count:
                result.append(k)

    result.sort()

    return result