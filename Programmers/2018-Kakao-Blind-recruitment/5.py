from collections import defaultdict


def solution(str1, str2):
    str1_list = []
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            str1_list.append(str1[i:i + 2])

    str2_list = []
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            str2_list.append(str2[i:i + 2])

    str1 = [x.lower() for x in str1_list]
    str2 = [x.lower() for x in str2_list]

    str1_set = set(str1)
    str2_set = set(str2)

    keys = str1_set.intersection(str2_set)
    _str1 = defaultdict(int)
    _str2 = defaultdict(int)

    for c in str1:
        _str1[c] += 1
    for c in str2:
        _str2[c] += 1

    a, b = 0, 0

    for key in keys:
        a += min(_str1[key], _str2[key])
        b += max(_str1[key], _str2[key])
        del (_str1[key])
        del (_str2[key])

    b += sum(_str1.values()) + sum(_str2.values())

    if b == 0:
        return 65536
    result = int(a * 65536 / b)

    return result
