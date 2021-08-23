import copy
from collections import deque

N, MAGIC_NUM = map(int, input().split())

n = 2 ** N
graph = [list(map(int, input().split())) for _ in range(n)]
magic_sizes = list(map(int, input().split()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def rotate(size, x, y):
    size_graph = copy.deepcopy(graph)

    for i in range(2 ** size):
        for j in range(2 ** size):
            nx = x + j
            ny = y + (2 ** size) - i - 1
            graph[nx][ny] = size_graph[x + i][y + j]


def melting():
    prev_graph = copy.deepcopy(graph)       # 이전 시점 얼음판

    for x in range(n):
        for y in range(n):
            if graph[x][y] <= 0:  # 이 위치에 얼음이 없는 경우 생략
                continue

            # 인접 얼음 개수 구하기
            cnt = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                if prev_graph[nx][ny] <= 0:
                    continue
                cnt += 1

            if cnt < 3:  # 주변 얼음이 3개 미만이면 녹음
                graph[x][y] -= 1


# bfs 로 얼음 덩어리 크기 구하기
# def bfs(x, y):
#     q = deque([(x, y)])
#     graph[x][y] = 0
#
#     cnt = 1
#
#     while q:
#         x, y = q.popleft()
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if nx < 0 or nx >= n or ny < 0 or ny >= n:
#                 continue
#
#             if graph[nx][ny] > 0:
#                 cnt += 1
#                 q.append((nx, ny))
#                 graph[nx][ny] = 0
#
#     return cnt


# dfs 로 얼음 덩어리 크기 구하기
def dfs(x, y):
    graph[x][y] = 0
    cnt = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if graph[nx][ny] > 0:
            cnt += dfs(nx, ny)
    return cnt

# 디버깅용 출력 함수
# def print_graph(graph):
#     for i in range(n):
#         print(graph[i])
#     print()


# 마법 순서대로 부리기
for size in magic_sizes:
    # 회전 시키기
    for i in range(0, n, 2 ** size):
        for j in range(0, n, 2 ** size):
            rotate(size, i, j)

    # 녹이기
    melting()
    # print_graph(graph)     # 디버깅용

# 얼음 총 개수
print(sum(sum(i) for i in graph))

# 얼음 덩어리 크기
max_iceland = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] > 0:
            max_iceland = max(max_iceland, dfs(i, j))

print(max_iceland)