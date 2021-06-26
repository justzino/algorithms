import re


def solution(new_id):
    string = new_id.lower()    # 1단계
    string = re.sub('[^a-z0-9\-_.]', '', string)    # 2단계
    string = re.sub('[.]+', '.', string)            # 3단계
    string = re.sub('^[.]|[.]$', '', string)        # 4단계
    string = 'a' if not string else string[:15]    # 5, 6단계
    string = re.sub('[.]$', '', string)
    while len(string) < 3:                          # 7단계
        string += string[-1]

    return string