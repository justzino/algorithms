def solution(info, query):
    lang = {'cpp': 0, 'java': 1, 'python': 2, '-': -1}
    app = {'backend': 0, 'frontend': 1, '-': -1}
    career = {'junior': 0, 'senior': 1, '-': -1}
    food = {'chicken': 0, 'pizza': 1, '-': -1}

    table = []
    for row in info:
        tmp = list(row.split())
        tmp[0] = lang[tmp[0]]
        tmp[1] = app[tmp[1]]
        tmp[2] = career[tmp[2]]
        tmp[3] = food[tmp[3]]
        tmp[4] = int(tmp[4])
        table.append(tmp)

    query_list = []
    for q in query:
        tmp = list(q.split(' and '))
        tmp[0] = lang[tmp[0]]
        tmp[1] = app[tmp[1]]
        tmp[2] = career[tmp[2]]

        f, s = tmp[3].split()
        tmp[3] = food[f]
        tmp.append(int(s))

        query_list.append(tmp)

    print(table)
    print(query_list)

    result = []
    for qur in query_list:
        search = 0
        for x in table:
            if not (qur[0] == -1 or x[0] == qur[0]):
                continue
            if not (qur[1] == -1 or x[1] == qur[1]):
                continue
            if not (qur[2] == -1 or x[2] == qur[2]):
                continue
            if not (qur[3] == -1 or x[3] == qur[3]):
                continue
            if x[4] >= qur[4]:
                search += 1
        result.append(search)

    return result
