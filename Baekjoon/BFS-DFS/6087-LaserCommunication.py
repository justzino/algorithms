import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs(loc, direction, count, start=False):
    global answer
    x, y = loc
    visited[x][y] = True

    for i in range(4):
        n_direction = (direction + i) % 4
        dx, dy = move[n_direction]
        nx = x + dx
        ny = y + dy

        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if visited[nx][ny]:
            continue
        # 도착한 경우
        if array[nx][ny] == 'C':
            if i == 0:
                answer = min(answer, count)
                return
            else:
                answer = min(answer, count+1)
                return
        if array[nx][ny] == '*':
            continue
        if start:
            dfs((nx, ny), n_direction, count)
            visited[nx][ny] = False  # 갔던길 돌아와서 방문 안한 처리 하기
        elif i == 0:
            dfs((nx, ny), n_direction, count)
            visited[nx][ny] = False     # 갔던길 돌아와서 방문 안한 처리 하기
        else:
            dfs((nx, ny), n_direction, count+1)
            visited[nx][ny] = False     # 갔던길 돌아와서 방문 안한 처리 하기


# main
"""
갈 수 있는 모든 경로 검색 -> 방향 전환 가장 적은 경로 선택 -> 거울 출력
"""
M, N = map(int, input().split())    # N, M이 반대로 들어오는 거 주의
array = []
visited = [[False] * M for _ in range(N)]
targets = []
answer = int(1e9)

for i in range(N):
    array.append(list(input()))
    for j in range(M):
        if array[i][j] == 'C':
            targets.append((i, j))

start, end = targets

# 경로 탐색
dfs(start, 0, 0, start=True)
print(answer)
