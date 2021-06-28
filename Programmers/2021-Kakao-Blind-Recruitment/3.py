from bisect import bisect_left


def solution(info, query):
    lang = {'cpp': 1, 'java': 2, 'python': 3, '-': 0}
    app = {'backend': 1, 'frontend': 2, '-': 0}
    career = {'junior': 1, 'senior': 2, '-': 0}
    food = {'chicken': 1, 'pizza': 2, '-': 0}

    table = {}

    for row in info:
        tmp = list(row.split())
        tmp[0] = lang[tmp[0]]
        tmp[1] = app[tmp[1]]
        tmp[2] = career[tmp[2]]
        tmp[3] = food[tmp[3]]
        score = int(tmp[4])

        for i in range(16):
            case = bin(i)[2:].zfill(4)
            string = str(tmp[0] * int(case[0])) + str(tmp[1] * int(case[1])) + str(tmp[2] * int(case[2])) + str(
                tmp[3] * int(case[3]))
            try:
                table[string].append(score)
            except:
                table[string] = [score]

    new_table = {}
    for key, value in table.items():
        value.sort()
        new_table[key] = value

    result = []
    for q in query:
        tmp = list(q.split(' and '))
        f, score = tmp[3].split()
        string = str(lang[tmp[0]]) + str(app[tmp[1]]) + str(career[tmp[2]]) + str(food[f])
        score = int(score)

        try:
            index = bisect_left(new_table[string], score)
            result.append(len(new_table[string]) - index)
        except:
            result.append(0)

    return result