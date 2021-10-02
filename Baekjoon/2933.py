import sys
from collections import deque, defaultdict
from bisect import bisect_left
input = sys.stdin.readline

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
MAX = 101


# 공중에 떠있는지 판단, bfs
def is_in_air(x, y, cluster):
    global R, C
    visited = [[False] * C for _ in range(R)]
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    flag = True
    while q:
        x, y = q.popleft()
        cluster.append((x, y))
        if x == R-1:
            flag = False
            break

        for dx, dy in move:
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                continue
            if visited[nx][ny]:
                continue
            if arr[nx][ny] != 'x':
                continue
            q.append((nx, ny))
            visited[nx][ny] = True
    return flag


# 공중에 떠있는 클러스터의 바닥 값들로부터 떠있는 높이 계산
def get_height_gap(cluster):
    global R, C
    bottom_cluster = defaultdict(int)   # dict[y] = x, 공중에 떠있는 클러스터의 가장 아래 좌표들
    min_gap = MAX

    for x, y in cluster:
        bottom_cluster[y] = max(bottom_cluster[y], x)
    for y, x in bottom_cluster.items():
        for tmp_x in range(x + 1, R):
            if arr[tmp_x][y] == 'x':    # y 열 가장 위에 나온 땅과 붙어있는 클러스터의 x
                min_gap = min(min_gap, tmp_x - x - 1)
                break
            if tmp_x == R-1:
                min_gap = min(min_gap, R - 1 - x)
    return min_gap


# 떠있는 높이 만큼 클러스터 떨어트림
def fall(gap, cluster):
    for x, y in cluster:
        arr[x][y] = '.'
    for x, y in cluster:
        arr[x+gap][y] = 'x'


# main
R, C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]

N = int(input())
height = list(map(int, input().split()))

# heights 에 있는 높이에서 막대기 던지기
for i in range(N):
    x = R - height[i]
    y = -1
    # left
    if i % 2 == 0:
        for j in range(C):      # 가장 왼쪽에 있는 위치 파괴
            if arr[x][j] == 'x':
                y = j
                break
    # right
    else:
        for j in range(C-1, -1, -1):    # 가장 오른쪽에 있는 위치 파괴
            if arr[x][j] == 'x':
                y = j
                break
    # 파괴 안된 경우 무시
    if y == -1:
        continue

    arr[x][y] = '.'         # 'x' -> '.'
    for dx, dy in move:
        nx = x + dx
        ny = y + dy
        new_cluster = []

        if nx < 0 or ny < 0 or nx >= R or ny >= C:
            continue
        if arr[nx][ny] != 'x':
            continue
        # 공중에 떠있는지 확인, new_cluster 에 새로운 cluster 저장
        in_air = is_in_air(nx, ny, new_cluster)
        if not in_air:
            continue
        # 바닥과 안붙어 있으면 -> 떨어트릴 높이 계산 -> 떨어트리기
        gap = get_height_gap(new_cluster)
        fall(gap, new_cluster)


for i in range(R):
    print("".join(arr[i]))
