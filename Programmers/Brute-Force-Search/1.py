A = [1, 2, 3, 4, 5]
B = [2, 1, 2, 3, 2, 4, 2, 5]
C = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]


def solution(answers):
    result_a, result_b, result_c = 0, 0, 0
    n = len(answers)

    a = A * (n // 5 + 1)
    b = B * (n // 8 + 1)
    c = C * (n // 10 + 1)

    for i in range(n):
        if answers[i] == a[i]: result_a += 1
        if answers[i] == b[i]: result_b += 1
        if answers[i] == c[i]: result_c += 1

    answer = []
    m = max(result_a, result_b, result_c)

    if m == result_a: answer.append(1)
    if m == result_b: answer.append(2)
    if m == result_c: answer.append(3)

    return answer


"""
1, 2, 3, 4, 5 -> 5개
2, 1, 2, 3, 2, 4, 2, 5 -> 8개
3, 3, 1, 1, 2, 2, 4, 4, 5, 5 -> 10개

[1, 2, 3] -> [1]
[1, 3, 3, 1] -> [1, 3]
[3, 3, 3, 4] -> [1, 3]
[]
"""