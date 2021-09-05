from collections import defaultdict
from bisect import bisect_left

# BIT_FIELD & BIT_MASK = code & (7 - code) = 0 -> 해당됨
BIT_FIELD = {
    "cpp": 1, "java": 2, "python": 4,
    "backend": 1, "frontend": 2,
    "junior": 1, "senior": 2,
    "chicken": 1, "pizza": 2,
    "-": 7
}


def preprocess(rows, is_query=False):
    new_rows = []

    for row in rows:
        values = [value for value in row.split(' ') if value != 'and']
        score = int(values[-1])
        code = 0

        for value in values[:-1]:
            if not is_query:
                code = (code << 3) + BIT_FIELD[value]  # BIT FIELD
            else:
                code = (code << 3) + (7 - BIT_FIELD[value])  # BIT_MASK

        new_rows.append((code, score))

    return new_rows


def solution(info, query):
    info = preprocess(info)
    query = preprocess(query, is_query=True)

    index = defaultdict(list)

    # info 정보 인덱싱
    for code, score in info:
        index[code].append(score)

    # 인덱싱된 점수 sort
    for code in index.keys():
        index[code].sort()

    # query 별 인원 세기
    answer = []
    for code, score in query:
        count = 0

        for key in index.keys():
            if code & key == 0:
                count += len(index[key]) - bisect_left(index[key], score)
        answer.append(count)

    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150",
        "cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100",
         "- and - and - and - 150"]
print(solution(info, query))