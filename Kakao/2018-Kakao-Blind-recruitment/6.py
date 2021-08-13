def get_remove_set(m, n, board):
    result = set()
    for i in range(n - 1):
        for j in range(m - 1):
            if board[i][j] == '0':
                continue
            if board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]:
                result.add((i, j))
                result.add((i + 1, j))
                result.add((i, j + 1))
                result.add((i + 1, j + 1))
    return result


def solution(m, n, board):
    new_board = ["".join(each) for each in zip(*board)]

    result = 0
    while True:
        removed_set = get_remove_set(m, n, new_board)
        if not removed_set:
            break

        for x, y in removed_set:
            new_board[x] = (new_board[x][:y] + 'x' + new_board[x][y + 1:])

        for i in range(n):
            new_board[i] = new_board[i].replace('x', '')
            new_board[i] = new_board[i].zfill(m)

        result += len(removed_set)

    return result
