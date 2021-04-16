n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


# DFS 로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나면 return
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    # 현재 노드를 방문하지 않았거나 현재 노드가 막혀있으면 return
    if graph[x][y] != 0:
        return False
    # 현재 노드 방문 처리
    graph[x][y] = 1

    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    return True


count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            count += 1

print(count)


# 4 5
# 0 0 1 1 0
# 0 0 0 1 1
# 1 1 1 1 1
# 0 0 0 0 0

# 15 14
# 0 0 0 0 0 1 1 1 1 0 0 0 0 0
# 1 1 1 1 1 1 0 1 1 1 1 1 1 0
# 1 1 0 1 1 1 0 1 1 0 1 1 1 0
# 1 1 0 1 1 1 0 1 1 0 0 0 0 0
# 1 1 0 1 1 1 1 1 1 1 1 1 1 1
# 1 1 0 1 1 1 1 1 1 1 1 1 0 0
# 1 1 0 0 0 0 0 0 0 1 1 1 1 1
# 0 1 1 1 1 1 1 1 1 1 1 1 1 1
# 0 0 0 0 0 0 0 0 0 1 1 1 1 1
# 0 1 1 1 1 1 1 1 1 1 1 0 0 0
# 0 0 0 1 1 1 1 1 1 1 1 0 0 0
# 0 0 0 0 0 0 0 1 1 1 1 0 0 0
# 1 1 1 1 1 1 1 1 1 1 0 0 1 1
# 1 1 1 0 0 0 1 1 1 1 1 1 1 1
# 1 1 1 0 0 0 1 1 1 1 1 1 1 1
