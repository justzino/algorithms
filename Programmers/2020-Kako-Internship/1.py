def get_distance(loc1, loc2):
    return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])


def get_mid_hand(q, r_hand, l_hand, hand):
    r = get_distance([q, 1], r_hand)
    l = get_distance([q, 1], l_hand)

    if r > l:
        return "L"
    elif l > r:
        return "R"

    if hand == "left":
        return "L"
    else:
        return "R"


def solution(numbers, hand):
    answer = ''
    r_hand = [3, 0]
    l_hand = [3, 2]

    for num in numbers:
        q, r = divmod(num, 3)
        if num == 0:
            if get_mid_hand(3, r_hand, l_hand, hand) == 'L':
                l_hand = [3, 1]
                answer += 'L'
            else:
                r_hand = [3, 1]
                answer += 'R'
        elif r == 2:
            if get_mid_hand(q, r_hand, l_hand, hand) == 'L':
                l_hand = [q, 1]
                answer += 'L'
            else:
                r_hand = [q, 1]
                answer += 'R'
        elif r == 0:
            answer += 'R'
            r_hand = [q - 1, 2]
        else:
            answer += 'L'
            l_hand = [q, 0]

    return answer