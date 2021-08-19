import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cmds = [tuple(map(int, input().split())) for _ in range(M)] # (방향, 이동거리)

# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]


# 구름 생성 -> 이동 -> 구름아래 물의양 증가
def move(direction, length):

    # 구름 이동
    for i in range(len(start)):
        x, y = start[i]
        nx = (x + dx[direction] * length) % N
        ny = (y + dy[direction] * length) % N
        start[i] = (nx, ny)
        visited[nx][ny] = True
        arr[nx][ny] += 1


# 대각선 방향 물 있는 칸 개수만큼 물복사
def copy_water():
    for x, y in start:
        # 대각선 방향
        for direction in range(1, 8, 2):
            nx = x + dx[direction]
            ny = y + dy[direction]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if arr[nx][ny] > 0:
                arr[x][y] += 1


def decrease():
    global start
    new_start = []
    for x in range(N):
        for y in range(N):
            if visited[x][y]:
                continue
            if arr[x][y] > 1:
                arr[x][y] -= 2
                new_start.append([x, y])
    start = new_start


# 구름 생성
start = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
for d, s in cmds:
    visited = [[False for _ in range(N)] for _ in range(N)]
    # 구름 이동 -> 구름아래 물의양 1 증가
    move(d-1, s)

    # 대각선 방향 물 있는 칸 개수만큼 물복사
    copy_water()

    # 그 외 물의 양이 2 이상인 칸의 물의양 2 감소
    decrease()

result = 0
for i in range(N):
    result += sum(arr[i])

print(result)
