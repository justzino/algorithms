import sys
sys.setrecursionlimit(100000)


def dfs(x, y):
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if cabbage[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny)


for _ in range(int(input())):
    m, n, k = map(int, input().split())

    cabbage = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        y, x = map(int, input().split())
        cabbage[x][y] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if cabbage[i][j] and not visited[i][j]:
                dfs(i, j)
                count += 1

    print(count)
