available_list = ['-', '_', '.']


def solution(new_id):
    answer = ''

    # 1단계
    tmp = new_id.lower()
    # 2단계
    for c in tmp:
        if c.islower() or c.isdigit() or c in available_list:
            answer += c
        else:
            continue

    # 3단계
    while answer.find("..") != -1:
        answer = answer.replace("..", '.')

        # 4, 5단계
    try:
        while answer[0] == ".":
            answer = answer[1:]
    except:
        answer += "a"
    try:
        while answer[-1] == ".":
            answer = answer[:-1]
    except:
        answer += "a"

    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == ".":
        answer = answer[:-1]

    # 7단계
    while len(answer) <= 2:
        answer += answer[-1]

    return answer
