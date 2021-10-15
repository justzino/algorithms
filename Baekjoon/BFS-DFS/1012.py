import sys
from collections import deque
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


def bfs(x, y):
    q = deque()
    q.append((x, y))
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        v = q.popleft()
        if not visited[v[0]][v[1]]:
            visited[v[0]][v[1]] = True
            for dx, dy in directions:
                nx, ny = v[0] + dx, v[1] + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if cabbage[nx][ny] and not visited[nx][ny]:
                    q.append((nx, ny))


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
                # dfs(i, j)
                bfs(i, j)
                count += 1

    print(count)
