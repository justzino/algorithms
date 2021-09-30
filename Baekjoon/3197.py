import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
MAP = []
bird_visited = [[False] * M for _ in range(N)]

move = [(0, 1), (1, 0), (0, -1), (-1, 0)]

bird_Q, bird_Next_Q = deque(), deque()      # 새 queue, 새 다음 queue
water_Q, water_Next_Q = deque(), deque()    # 물 queue, 물 다음 queue
birds = []      ##### 시작위치뿐만 아니라, 반대편 백조도 포함시키기 위함으로 추가했습니다.

for x in range(N):
    line = list(input().rstrip())
    for y in range(M):
        if line[y] != 'X':      # 얼음 아니면 전부 물 queue에 넣기
            water_Q.append((x, y))
        if line[y] == 'L':      # L, 백조 위치
            start_bird = (x, y)
            birds.append((x, y))
            line[y] = '.'       #### 사실상 백조를 다른데에 저장을 해두면, 굳이 L로 구분할 필요가 없기에 뺐습니다.
    MAP.append(line)

start_bird, end_bird = birds    # 시작 백조와 아닌 백조를 구분
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
                    bird_Q.append((nx, ny))
                elif MAP[nx][ny] == 'X':
                    bird_Next_Q.append((nx, ny))
                #### 백조가 맞닿은 얼음은 곧 녹을거기때문에, 그냥 같이 방문처리를 해주었습니다.
                bird_visited[nx][ny] = True


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
    bird_Q = bird_Next_Q     # 새로 확장한 영역만 bird_bfs 돌리기 위해
    bird_Next_Q = deque()
    ## 만약 다른 새가 마주쳤다면, 멈춥니다.
    if bird_visited[end_bird[0]][end_bird[1]]:
        break

    water_bfs()
    water_Q = water_Next_Q   # 새로 확장한 영역만 water_bfs 돌리기 위해
    water_Next_Q = deque()
    day += 1

print(day)
