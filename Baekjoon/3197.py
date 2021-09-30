import sys
from collections import deque
import copy
input = sys.stdin.readline

N, M = map(int, input().split())
MAP = []
bird_visited = [[False] * M for _ in range(N)]

move = [(0, 1), (1, 0), (0, -1), (-1, 0)]

bird_Q, bird_Next_Q = deque(), deque()      # 새 queue, 새 다음 queue
water_Q, water_Next_Q = deque(), deque()    # 물 queue, 물 다음 queue
start_bird = (int, int)     # 새 한마리 위치

for x in range(N):
    line = list(input().rstrip())
    MAP.append(line)
    for y in range(M):
        if line[y] != 'X':      # 얼음 아니면 전부 물 queue에 넣기
            water_Q.append((x, y))
        if line[y] == 'L':      # L, 백조 위치
            start_bird = (x, y)

melting_list = []


def bird_bfs():
    global find
    while bird_Q and not find:
        x, y = bird_Q.popleft()

        for dx, dy in move:
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if not bird_visited[nx][ny]:
                if MAP[nx][ny] == '.':
                    bird_visited[nx][ny] = True
                    bird_Q.append((nx, ny))
                elif MAP[nx][ny] == 'X':
                    bird_Next_Q.append((nx, ny))
                elif MAP[nx][ny] == 'L':
                    bird_visited[nx][ny] = True
                    find = True
                    break


def water_bfs():
    while water_Q:
        x, y = water_Q.popleft()

        for dx, dy in move:
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            # 새로 만난 빙판 부분 water_Next_Q 에 삽입, 녹이기
            if MAP[nx][ny] == 'X':
                MAP[nx][ny] = '.'
                water_Next_Q.append((nx, ny))


day = 0
bird_Q.append(start_bird)
bird_visited[start_bird[0]][start_bird[1]] = True
find = False

while not find:
    bird_bfs()
    bird_Q = copy.deepcopy(bird_Next_Q)     # 새로 확장한 영역만 bird_bfs 돌리기 위해
    bird_Next_Q.clear()

    if not find:
        water_bfs()
        water_Q = copy.deepcopy(water_Next_Q)   # 새로 확장한 영역만 water_bfs 돌리기 위해
        water_Next_Q.clear()
        day += 1

print(day)
