def solution(n, computers):
    adj = [[] for _ in range(n)]

    for i in range(n):
        for j in range(i+1, n):
            if computers[i][j]:
                adj[i].append(j)
                adj[j].append(i)

    def dfs(v):
        if not visited[v]:
            visited[v] = True
            for edge in adj[v]:
                dfs(edge)

    cnt = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(i)
            cnt += 1

    return cnt


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))
