def convert_title(file):
    head = file.lower()
    number, tail = '', ''

    for i in range(len(file)):
        if head[i].isdigit():
            head, number = head[:i], head[i:]
            break

    if number:
        for i in range(len(number)):
            if not number[i].isdigit():
                number, tail = number[:i], number[i:]
                break
        number = int(number)
    else:
        number = 0

    # print(head, number, tail)
    return (head, number)


def solution(files):
    result = sorted(files, key=convert_title)

    return result


"""
HEAD, NUMBER, TAIL
NUMBER : 12, 012 는 같은 파일이지만, 입력순서 지켜서 sorting
"""