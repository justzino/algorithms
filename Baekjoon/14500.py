import sys
input = sys.stdin.readline

blocks = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 1)]
]


def bfs(x, y, block):
    count = 0

    for dx, dy in block:
        nx = x + dx
        ny = y + dy

        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            count = 0
            break
        count += graph[nx][ny]
    return count


def rotate_90_degree():
    n = len(graph)
    m = len(graph[0])
    new_graph = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_graph[j][n-1-i] = graph[i][j]
    return new_graph


def symmetry(horizon):
    n = len(graph)
    m = len(graph[0])
    new_graph = [[0] * m for _ in range(n)]
    if horizon == 0:    # 가로축 대칭
        for i in range(n):
            for j in range(m):
                new_graph[i][j] = graph[n-1-i][j]

    else:               # 세로축 대칭
        for i in range(n):
            for j in range(m):
                new_graph[i][j] = graph[i][m-1-j]
    return new_graph


# main
N, M = map(int, input().split())
graph = []
visited = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

cnt = 0
for r in range(4):
    graph = rotate_90_degree()
    N = len(graph)
    M = len(graph[0])
    for d in range(4):
        graph = symmetry(d)
        visited = [[False] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if visited[i][j]:
                    continue
                cnt = max(cnt, bfs(i, j, blocks[0]))
                cnt = max(cnt, bfs(i, j, blocks[1]))
                cnt = max(cnt, bfs(i, j, blocks[2]))
                cnt = max(cnt, bfs(i, j, blocks[3]))
                cnt = max(cnt, bfs(i, j, blocks[4]))
                visited[i][j] = True

print(cnt)