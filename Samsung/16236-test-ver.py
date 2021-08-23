import sys, copy
sys.setrecursionlimit(10**8)

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗ : 8방향
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

graph = [[] for _ in range(4)]     # (물고기 숫자, 방향 번호)
fishes = [(0, 0) for _ in range(17)]     # fishes[i] = (x, y)

# directions = [[] for _ in range(4)]

for i in range(4):
    line = list(map(int, input().split()))
    for j in range(4):
        graph[i].append((line[2 * j], line[2 * j + 1] - 1))
        fishes[line[2 * j]] = (i, j)


# 물고기 이동
def move_fishes(graph, fishes):
    # 물고기 16마리에 대해
    for i in range(1, 17):
        fx, fy = fishes[i]      # 현재 물고기 위치
        fd = graph[fx][fy][1]   # 현재 물고기 방향

        if fx == -1:       # 잡아 먹힌 경우
            continue

        for _ in range(8):
            # 물고기 이동 (swap)
            nfx, nfy = fx + dx[fd], fy + dy[fd]
            # 가려는 곳이 벽인 경우
            if nfx < 0 or nfx > 3 or nfy < 0 or nfy > 3:
                fd = (fd + 1) % 8   # 45도 반시계 회전
                continue
            # 가려는 곳에 상어가 있는 경우
            if graph[nfx][nfy][0] == -1:
                fd = (fd + 1) % 8  # 45도 반시계 회전
                continue
            # 가려는 곳이 비어있는 경우 swap
            elif graph[nfx][nfy][0] == 0:
                fishes[i] = (nfx, nfy)
                graph[nfx][nfy], graph[fx][fy] = (i, fd), graph[nfx][nfy]
                break

            # 가려는 곳에 물고기가 있는 경우
            else:
                fishes[i], fishes[graph[nfx][nfy][0]] = (nfx, nfy), (fx, fy)
                graph[nfx][nfy], graph[fx][fy] = (i, fd), graph[nfx][nfy]
                break


# (0, 0) 상어 입성
x, y, d = 0, 0, graph[0][0][1]  # 상어: (x, y, 방향)
eat = graph[0][0][0]
max_eat = eat
print(f"상어 위치 : ({x}, {y}), 먹은 물고기 넘버: {eat}, 여태 먹은 총 물고기 합: {max_eat}")

fishes[graph[0][0][0]] = (-1, -1)       # 잡아 먹히면 (-1, -1)
graph[0][0] = (-1, graph[0][0][1])      # 상어 (-1, 방향) or 비어 있으면 (0, 0)


# 상어 이동
def dfs(sx, sy, sd, graph, fishes):
    global eat, max_eat

    move_fishes(graph, fishes)   # 물고기 이동
    print(f"<물고기 이동>")
    graph_print(graph)

    for i in range(1, 4):
        # 상어 이동 거리
        nx, ny = sx + dx[sd] * i, sy + dy[sd] * i

        # 가려는 곳이 벽인 경우
        if nx < 0 or nx > 3 or ny < 0 or ny > 3:
            return

        # 비어 있는 경우
        if graph[nx][ny][0] == 0:
            continue

        # 백트래킹을 위한 이전 정보 저장
        new_graph = copy.deepcopy(graph)
        new_fishes = fishes[:]
        dead_fish = new_graph[nx][ny]               # 죽기전 물고기의 (번호, 방향)

        # 물고기 있는 경우 이동, 잡아먹음
        eat += new_graph[nx][ny][0]
        max_eat = max(max_eat, eat)

        # 변화 시작
        new_fishes[new_graph[nx][ny][0]] = (-1, -1)     # 물고기 죽음
        new_graph[sx][sy] = (0, 0)      # 이전 상어 위치
        new_graph[nx][ny] = (-1, dead_fish[1])     # 움직인 위치에 상어 존재

        print(f"<상어 이동>")
        print(f"상어 위치 : ({nx}, {ny}), 먹은 물고기 넘버: {dead_fish[0]}, 여태 먹은 총 물고기 합: {eat}")
        graph_print(new_graph)

        dfs(nx, ny, dead_fish[1], new_graph, new_fishes)

        # 잡아먹으러 움직이기 전으로 Back-tracking
        eat -= dead_fish[0]
        # graph[sx][sy] = (-1, 0)
        # graph[nx][ny] = dead_fish
        # fishes[dead_fish[0]] = (nx, ny)

        print()
        print(f"상어 위치 : ({sx}, {sy}), 뱉은 물고기 넘버: {dead_fish[0]}, 여태 먹은 총 물고기 합: {eat},        [{graph[sx][sy][0]} == -1] 인지 확인")


def graph_print(graph):
    dd = ['↑', '↖', "←", '↙', '↓', '↘', '→', '↗']

    tmp_graph = copy.deepcopy(graph)

    for i in range(4):
        for j in range(4):
            tmp_graph[i][j] = (tmp_graph[i][j][0], dd[tmp_graph[i][j][1]])

        print(tmp_graph[i])


graph_print(graph)
dfs(x, y, d, graph[:], fishes[:])

print(max_eat)

