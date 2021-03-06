from itertools import permutations


def solution(n, weak, dist):
    length = len(weak)

    for i in range(length):
        weak.append(weak[i] + n)        # 원형 큐 대신, list 를 이어붙여서 사용

    result = len(dist) + 1      # 투입할 수 있는 친구 MAX 값 저장

    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1       # 투입할 친구 수
            position = weak[start] + friends[count - 1]        # 커버할 수 있는 포지션

            for i in range(start, start + length):
                if position < weak[i]:
                    count += 1
                    if count > len(friends):
                        break
                    position = weak[i] + friends[count - 1]    # 중간 간격 한 칸 건너 뛰고 친구가 커버

            result = min(result, count)

    if result > len(dist):
        return -1

    return result


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
