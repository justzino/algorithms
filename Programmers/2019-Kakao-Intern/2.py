def solution(s):
    s = s[2:-2]
    s_lst = s.split('},{')
    s_lst = sorted(s_lst, key=lambda x: len(x))

    tuples = []
    for x in s_lst:
        tuples.append(set(map(int, x.split(','))))

    result = list(tuples[0])
    for i in range(len(tuples) - 1):
        next = list(tuples[i + 1] - tuples[i])
        result.extend(next)

    return result
