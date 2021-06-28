def solution(info, query):
    # lang = {'cpp': 0, 'java': 1, 'python': 2}
    # app = {'backend': 0, 'frontend': 1}
    # career = {'junior': 0, 'senior': 1}
    # food = {'chicken': 0, 'pizza': 1}

    table = []
    for row in info:
        tmp = list(row.split())
        tmp[-1] = int(tmp[-1])
        table.append(tmp)

    query_list = []
    for q in query:
        row = list(q.split(' and '))
        f, s = row[-1].split()
        row[-1] = f
        row.append(int(s))
        query_list.append(row)

    result = []
    for case in query_list:
        if case[0] == '-':
            search = table
        else:
            search = [x for x in table if x[0] == case[0]]
        if case[1] == '-':
            pass
        else:
            search = [x for x in search if x[1] == case[1]]
        if case[2] == '-':
            pass
        else:
            search = [x for x in search if x[2] == case[2]]
        if case[3] == '-':
            pass
        else:
            search = [x for x in search if x[3] == case[3]]
        search = [x for x in search if x[4] >= case[4]]

        result.append(len(search))

    return result