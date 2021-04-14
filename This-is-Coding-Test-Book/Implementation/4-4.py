n, m = map(int, input().split())
x, y, d = map(int, input().split())
map_matrix = [[] for _ in range(n)]

for i in range(n):
    map_matrix[i] = list(map(int, input().split()))

# 0: 북, 1: 동, 2: 남, 3: 서
# 바라보는 방향: 북, 서, 남, 동
directions = [0, 3, 2, 1]

# 이동 방향: 서, 남, 동, 북
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

nx, ny = 0, 0
count = 0
turn_time = 0

while True:
    for i in range(4):
        turn_time += 1
        if d != directions[i]:
            continue

        nx = x + dx[i]
        ny = y + dy[i]
        d = (i + 1) % 3

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue

        if map_matrix[nx][ny] == 1:
            continue

        map_matrix[nx][ny] = 1
        x = nx
        y = ny
        turn_time = 0
        break

    if turn_time == 4:
        break

print(count)

# 입력
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1
