from itertools import combinations


def judge(place, t1, t2):
    x_dist = t2[0] - t1[0]
    y_dist = t2[1] - t1[1]
    distance = abs(x_dist) + abs(y_dist)

    if distance > 2:
        return True

    if distance == 1:
        return False

    if x_dist == 2:
        if place[t1[0] + 1][t1[1]] == 'X':
            return True
        return False
    if x_dist == -2:
        if place[t1[0] - 1][t1[1]] == 'X':
            return True
        return False
    if y_dist == 2:
        if place[t1[0]][t1[1] + 1] == 'X':
            return True
        return False
    if y_dist == -2:
        if place[t1[0]][t1[1] - 1] == 'X':
            return True
        return False

    if place[t1[0] + x_dist][t1[1]] == 'X' and place[t1[0]][t1[1] + y_dist] == 'X':
        return True
    else:
        return False


def solution(places):
    results = []

    for place in places:
        room = [[-1] * 5 for _ in range(5)]
        persons = []

        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    persons.append((i, j))
                room[i][j] = place[i][j]

        cases = list(combinations(persons, 2))

        result = 1
        for case in cases:
            if judge(room, case[0], case[1]):
                continue
            else:
                result = 0
                break

        results.append(result)

    return results


# P,O,X

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
