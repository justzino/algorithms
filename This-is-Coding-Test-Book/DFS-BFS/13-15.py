from collections import deque
import sys

input = sys.stdin.readline
MAX = 1e9


def bfs(s):
    q = deque([s])
    visited[s] = 0

    while q:
        v = q.popleft()
        if visited[v] > goal:
            continue
        for node in graph[v]:
            if visited[v] + 1 < visited[node]:
                visited[node] = visited[v] + 1
                q.append(node)


n_city, n_path, goal, start = map(int, input().split())
graph = [[] for _ in range(n_city + 1)]


for _ in range(n_path):
    a, b = map(int, input().split())
    graph[a].append(b)


visited = [MAX] * (n_city + 1)
bfs(start)

count = 0
for i in range(1, n_city + 1):
    if visited[i] == goal:
        count += 1
        print(i)

if count == 0:
    print(-1)
