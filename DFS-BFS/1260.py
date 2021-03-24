# 1260 DFS 와 BFS
from collections import deque


n, m, v = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

for e in adj:
    e.sort()


def dfs(vertex):
    print(vertex, end=' ')
    visited[vertex] = True
    for edge in adj[vertex]:
        if not visited[edge]:
            dfs(edge)


def bfs(vertex):
    q = deque([vertex])
    while q:
        vertex = q.popleft()
        if not visited[vertex]:
            visited[vertex] = True
            print(vertex, end=' ')
            for edge in adj[vertex]:
                if not visited[edge]:
                    q.append(edge)


visited = [False] * (n+1)
dfs(v)
print()

visited = [False] * (n+1)
bfs(v)
