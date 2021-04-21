import heapq

INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

x, k = map(int, input().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node in graph[now]:
            cost = dist + 1
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(q, (cost, node))


distance = [INF] * (n + 1)
dijkstra(1)
dist_k = distance[k]

distance = [INF] * (n + 1)
dijkstra(k)
dist_x = distance[x]

time = dist_k + dist_x
if time < INF:
    print(time)
else:
    print(-1)

# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5
# 결과: 3

# 4 2
# 1 3
# 2 4
# 3 4
# 결과: -1
