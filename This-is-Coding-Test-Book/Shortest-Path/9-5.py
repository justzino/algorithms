import heapq

INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    # a -> b : dist 만큼 시간
    a, b, dist = map(int, input().split())
    # graph[a] : [(dist1, node1), (dist2, node2), ...]
    graph[a].append((dist, b))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node in graph[now]:
            cost = dist + node[0]
            if cost < distance[node[1]]:
                distance[node[1]] = cost
                heapq.heappush(q, (cost, node[1]))


dijkstra(c)

count = 0
time = 0

for i in range(1, n + 1):
    cost = distance[i]
    if cost < INF:
        count += 1
        time = max(time, cost)

print(count, time)
