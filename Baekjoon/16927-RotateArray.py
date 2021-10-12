import math
from collections import deque
moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]


# 옮길 테두리 값들 구하기
def search(start_x, start_y):
    global N, M
    x, y = start_x, start_y
    q = deque([])
    q.append(array[x][y])

    for dx, dy in moves:
        while True:
            nx = x + dx
            ny = y + dy
            if nx < start_x or ny < start_y or nx >= N-start_x or ny >= M-start_y:
                break
            if visited[nx][ny]:
                break
            q.append(array[nx][ny])
            visited[nx][ny] = True
            x, y = nx, ny
    return q


def rotate(n, k):
    global N, M
    # k 만큼 돌려서 넣기 시작할 위치 구하기
    x, y = n, n
    d = 0
    for _ in range(k):
        nx = x + moves[d][0]
        ny = y + moves[d][1]

        if nx < n or ny < n or nx >= N - n or ny >= M - n:
            d = (d+1) % 4
            nx = x + moves[d][0]
            ny = y + moves[d][1]

        x, y = nx, ny

    # 큐 구한후, 시작위치부터 넣기
    q = search(n, n)
    while q:
        v = q.popleft()
        array[x][y] = v

        nx = x + moves[d][0]
        ny = y + moves[d][1]

        if nx < n or ny < n or nx >= N - n or ny >= M - n:
            d = (d + 1) % 4
            nx = x + moves[d][0]
            ny = y + moves[d][1]

        x, y = nx, ny


N, M, R = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

for i in range(math.ceil(min(N, M)/2)):
    k = R % ((N-2*i)*2 + (M-2*i)*2 - 4)    # 가로길이*2 + 세로길이*2 - 4 로 나눈 나머지만큼 이동
    rotate(i, k)

for i in range(N):
    print(*array[i])