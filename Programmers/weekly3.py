import copy

N = 0
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs(graph, x, y, start_point, finding_num):
    global N

    graph[x][y] = 2
    result = [start_point]  # [0, 0] 기준으로 block들 shift 시켜서 저장 후 return

    for dx, dy in move:
        nx = x + dx
        ny = y + dy

        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        if graph[nx][ny] != finding_num:
            continue
        result += dfs(graph, nx, ny, [start_point[0] + dx, start_point[1] + dy], finding_num)

    return result


def rotate_90_degree(graph):
    global N
    rotated_graph = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            rotated_graph[i][j] = graph[j][N - 1 - i]

    return rotated_graph


def solution(game_board, table):
    global N
    N = len(game_board)

    blocks = []

    finding_num = 0  # game_board 에서는 0인 부분을 찾아야 함
    start_point = [0, 0]
    for i in range(N):
        for j in range(N):
            if game_board[i][j] != finding_num:
                continue
            block = dfs(game_board, i, j, start_point, finding_num)
            blocks.append(block)

    finding_num = 1
    answer = 0
    for _ in range(4):
        table = rotate_90_degree(table)
        rotated_table = copy.deepcopy(table)

        for i in range(N):
            for j in range(N):
                if rotated_table[i][j] != finding_num:
                    continue
                puzzle = dfs(rotated_table, i, j, start_point, finding_num)

                if puzzle in blocks:
                    blocks.pop(blocks.index(puzzle))
                    answer += len(puzzle)

                    table = copy.deepcopy(rotated_table)
                else:
                    rotated_table = copy.deepcopy(table)

    return answer


game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
print(solution(game_board, table))