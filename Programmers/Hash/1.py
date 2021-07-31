from collections import defaultdict


def solution(participant, completion):
    parti_hash = defaultdict(int)
    for p in participant:
        parti_hash[p] += 1

    for c in completion:
        parti_hash[c] -= 1

    answer = ''
    for key, value in parti_hash.items():
        if value > 0:
            answer = key

    return answer