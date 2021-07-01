def solution(record):
    commands_set = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}

    name_dict = dict()
    record_by_id = []

    for string in record:
        string = string.split()
        command = string[0]
        uid = string[1]

        if len(string) != 2:
            name_dict[uid] = string[2]

        record_by_id.append((uid, command))

    result = []
    for uid, command in record_by_id:
        if command == 'Change':
            continue
        else:
            result.append(name_dict[uid] + commands_set[command])

    return result