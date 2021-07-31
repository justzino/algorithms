from collections import defaultdict


def solution(clothes):
    num_by_part = defaultdict(int)
    for cloth in clothes:
        num_by_part[cloth[1]] += 1

    answer = 1
    for num in num_by_part.values():
        answer *= (num + 1)

    answer -= 1
    return answer


"""
문자열 : 1 <= c <= 20, 소문자, '_'
최소 한개 의상
"""