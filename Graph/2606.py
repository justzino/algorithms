n = int(input())
c = int(input())

adj = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(c):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)


def dfs(v):
    global count
    for edge in adj[v]:
        if not visited[edge]:
            visited[edge] = True
            count += 1
            dfs(edge)


count = 0
dfs(1)
print(count-1)
