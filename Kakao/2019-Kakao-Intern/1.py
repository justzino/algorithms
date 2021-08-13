def solution(board, moves):
    n = len(board)
    stacks = list(map(list, zip(*board)))
    for i in range(n):
        stacks[i].reverse()
    result = []
    answer = 0

    for move in moves:
        try:
            while True:
                tmp = stacks[move - 1].pop()
                if tmp != 0:
                    break

            if tmp == 0:
                continue
            if result and tmp == result[-1]:
                print(result[-1], tmp)
                result.pop()
                answer += 2
            else:
                result.append(tmp)
        except:
            continue

    return answer