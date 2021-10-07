from itertools import product


def solution(word):
    alph = ['', 'A', 'E', 'I', 'O', 'U']

    string = list(map(list, product(alph, repeat=4)))
    new_cases = []
    for i in range(len(string)):
        new_cases.append(''.join(string[i]))
    new_cases = list(set(new_cases))
    new_cases.sort()

    start = word[0]
    ends = word[1:]

    count = 0
    turn_cnt = len(new_cases)

    for i in range(6):
        if start == alph[i]:
            count += turn_cnt * (i - 1)

    extra_cnt = new_cases.index(ends)
    count += extra_cnt + 1

    return count