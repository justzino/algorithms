#   |  0   1   2
# --+------------
# 0 |  0   7   5
# 1 |  7   0  INF
# 2 |  5  INF  0

INF = 1e9

# Adjacent Matrix
graph1 = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]


# Adjacent List
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))
# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0, 7))
# 노드 2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0, 5))

