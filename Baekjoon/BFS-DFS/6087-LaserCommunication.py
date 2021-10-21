import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(start, end):
    x, y = start
    q = deque([(x, y, 0), (x, y, 1), (x, y, 2), (x, y, 3)])     # (x, y, 방향)
    cost[x][y] = 0

    while q:
        x, y, direction = q.popleft()
        for d in range(4):
            new_d = (direction + d) % 4
            nx = x + move[new_d][0]
            ny = y + move[new_d][1]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:      # array 벗어난 경우
                continue
            if array[nx][ny] == '*':        # 벽인 경우
                continue

            # 같은 방향이면 cost 추가 x
            if direction == new_d:
                # 목적지 도착한 겨우
                # if nx == end[0] and ny == end[1]:
                #     cost[nx][ny] = min(cost[nx][ny], cost[x][y])
                #     break

                # cost 변경 되면 q에 추가
                if cost[x][y] <= cost[nx][ny]:
                    cost[nx][ny] = cost[x][y]
                    q.append((nx, ny, new_d))

            # 다른 방향이면 cost + 1
            else:
                # 목적지 도착한 겨우
                # if nx == end[0] and ny == end[1]:
                #     cost[nx][ny] = min(cost[nx][ny], cost[x][y]+1)
                #     break
                # cost 변경 되면 q에 추가
                if cost[x][y] + 1 <= cost[nx][ny]:
                    cost[nx][ny] = cost[x][y] + 1
                    q.append((nx, ny, new_d))


# main
M, N = map(int, input().split())    # N, M이 반대로 들어오는 거 주의
array = []
MAX = int(1e9)
cost = [[MAX] * M for _ in range(N)]
targets = []
answer = MAX

for i in range(N):
    array.append(list(input().rstrip()))
    for j in range(M):
        if array[i][j] == 'C':
            targets.append((i, j))

start, end = targets

# 경로 탐색
bfs(start, end)
print(cost[end[0]][end[1]])

"""
5 5
C..**
.*.**
.*...
.***C
.....

>>> 2


4 6
.C..
....
....
**.*
....
...C

>>> 2
"""