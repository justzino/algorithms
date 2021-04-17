from collections import deque


n, m = map(int, input().split())
graph = []
dp = [[1e9] * m for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, input().split())))


def bfs(x, y):
    q = deque()
    q.append((x, y))

    visited[x][y] = True
    dp[x][y] = 1

    while q:
        v = q.popleft()
        x, y = v[0], v[1]

        if x < n-1 and graph[x+1][y] == 1:
            visited[x+1][y] = True
            dp[x+1][y] = min(dp[x+1][y], dp[x][y] + 1)
            q.append((x+1, y))

        if y < m-1 and graph[x][y+1] == 1:
            visited[x][y+1] = True
            dp[x][y+1] = min(dp[x+1][y], dp[x][y] + 1)
            q.append((x, y+1))


visited = [[False] * m for _ in range(n)]
bfs(0, 0)

print(dp[n-1][m-1])

# 5 6
# 1 0 1 0 1 0
# 1 1 1 1 1 1
# 0 0 0 0 0 1
# 1 1 1 1 1 1
# 1 1 1 1 1 1
