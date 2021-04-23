# 미완성/못품...ㅠㅠ
from collections import deque

n = int(input())

indegree = [0] * (n + 1)
cost = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    time, *nodes = map(int, input().split())
    cost[i] = time
    indegree[i] = len(nodes - 1)
    for node in nodes:
        if node == -1:
            break
        graph[node].append(i)


def topology_sort():
    result = 0
    q = deque()
    for lecture in graph:
        if indegree[lecture] == 0:
            q.append(lecture)
    result += max(cost)

    while q:
        now = q.popleft()
        for after_lecture in graph[now]:
            indegree[after_lecture] -= 1
            if indegree[after_lecture] == 0:
                q.append(after_lecture)
