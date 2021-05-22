from collections import deque


# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def widen(virus, time):
    while virus:
        num, x, y, t = virus.popleft()
        if t == time:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if matrix[nx][ny] > 0:
                continue
            matrix[nx][ny] = num
            virus.append([num, nx, ny, t + 1])


n, k = map(int, input().split())

matrix = []
q = []
for i in range(n):
    tmp = list(map(int, input().split()))
    matrix.append(tmp)
    for j in range(n):
        if tmp[j] > 0:
            q.append([tmp[j], i, j, 0])

q.sort()
q = deque(q)

time, x, y = map(int, input().split())

widen(q, time)

print(matrix[x-1][y-1])
