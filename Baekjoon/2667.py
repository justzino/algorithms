import sys
input = sys.stdin.readline


N = int(input())
arr = [input().strip() for _ in range(N)]

visited = [[False] * N for _ in range(N)]
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs(x, y):
    global count
    count += 1
    visited[x][y] = True

    for dx, dy in move:
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        if visited[nx][ny]:
            continue
        if arr[nx][ny] == '0':
            continue
        dfs(nx, ny)


result = []
count = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] or arr[i][j] == '0':
            continue
        count = 0
        dfs(i, j)
        result.append(count)

result.sort()
print(len(result))
for r in result:
    print(r)
