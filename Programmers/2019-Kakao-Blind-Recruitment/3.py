from itertools import combinations


# 유일성 판단 : 유일성 만족 후보키인지 True/False return
def is_identical(relation, key):
    _relation = []
    for record in relation:
        code = ''
        for column in key:
            code += str(record[column])
        _relation.append(code)

    result = True
    for code in _relation:
        if _relation.count(code) > 1:
            result = False
            break

    return result


# 최소성 판단 : 최소성 만족한 후보키들 개수 return
def is_minimal(keys):
    if not keys:
        return 0

    key_codes = []
    for key in keys:
        code = ''
        for i in key:
            code += str(i)
        key_codes.append(code)

    minimal_keys = key_codes[:]

    n = len(key_codes)
    for i in range(n):
        for j in range(i + 1, n):
            n_code = len(key_codes[i])  # key_codes[j] 에 key_codes[i] 가 전부 있는지 판단
            for x in key_codes[i]:
                if x in key_codes[j] and key_codes[j] in minimal_keys:
                    n_code -= 1
            if n_code < 1:
                minimal_keys.remove(key_codes[j])

    result = len(minimal_keys)

    return result


def solution(relation):
    n_row = len(relation[0])
    rows = [i for i in range(n_row)]
    all_keys = []

    for i in range(1, n_row + 1):
        keys = list(combinations(rows, i))
        all_keys += keys

    super_keys = []

    for key in all_keys:
        if is_identical(relation, key):
            super_keys.append(key)

    candidate_keys = is_minimal(super_keys)

    return candidate_keys
