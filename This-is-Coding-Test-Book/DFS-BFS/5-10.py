n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))


def dfs(x, y):
    # 주어진 범위를 벗어나면 return
    if x < 0 or y < 0 or x >= n or y >= m:
        return
    # 현재 노드를 방문하지 않았으면 return
    if visited[x][y]:
        return
    # 현재 노드가 막혀있으면 return
    if graph[x][y] == 1:
        return

    visited[x][y] = True

    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)


visited = [[False] * m for _ in range(n)]

count = 0
for i in range(n):
    for j in range(m):
        if (not visited[i][j]) and graph[i][j] == 0:
            dfs(i, j)
            count += 1

print(count)


# 4 5
# 0 0 1 1 0
# 0 0 0 1 1
# 1 1 1 1 1
# 0 0 0 0 0

# 15 14
# 0 0 0 0 0 1 1 1 1 0 0 0 0 0
# 1 1 1 1 1 1 0 1 1 1 1 1 1 0
# 1 1 0 1 1 1 0 1 1 0 1 1 1 0
# 1 1 0 1 1 1 0 1 1 0 0 0 0 0
# 1 1 0 1 1 1 1 1 1 1 1 1 1 1
# 1 1 0 1 1 1 1 1 1 1 1 1 0 0
# 1 1 0 0 0 0 0 0 0 1 1 1 1 1
# 0 1 1 1 1 1 1 1 1 1 1 1 1 1
# 0 0 0 0 0 0 0 0 0 1 1 1 1 1
# 0 1 1 1 1 1 1 1 1 1 1 0 0 0
# 0 0 0 1 1 1 1 1 1 1 1 0 0 0
# 0 0 0 0 0 0 0 1 1 1 1 0 0 0
# 1 1 1 1 1 1 1 1 1 1 0 0 1 1
# 1 1 1 0 0 0 1 1 1 1 1 1 1 1
# 1 1 1 0 0 0 1 1 1 1 1 1 1 1
