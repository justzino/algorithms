from collections import deque
from itertools import combinations
import copy


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

row, column = map(int, input().split())


def infect(matrix, start):
    q = deque([start])

    while q:
        x, y = q.popleft()

        for i in range(4):
            if x + dx[i] < 0 or x + dx[i] >= row or y + dy[i] < 0 or y + dy[i] >= column:
                continue
            if matrix[x + dx[i]][y + dy[i]] == 0:
                q.append([x + dx[i], y + dy[i]])
                matrix[x + dx[i]][y + dy[i]] = 2


def safe_zone(matrix):
    count = 0
    for line in matrix:
        count += line.count(0)

    return count


graph = [[] for _ in range(row)]
infected = []
for i in range(row):
    tmp = list(map(int, input().split()))
    graph[i] = tmp
    for j in range(column):
        if tmp[j] == 2:
            infected.append([i, j])

index = []
for j in range(column):
    for i in range(row):
        if graph[i][j] == 0:
            index.append([i, j])

cases = list(combinations(index, 3))
result = 0

for case in cases:
    copyGraph = copy.deepcopy(graph)
    for i, j in case:
        copyGraph[i][j] = 1

    for virus in infected:
        infect(copyGraph, virus)

    result = max(result, safe_zone(copyGraph))

print(result)