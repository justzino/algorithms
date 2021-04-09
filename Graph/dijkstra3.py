import heapq
import sys


input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)

for _ in range(e):
    a, b, c = map(int, input().split())
    # a번 노드에서 c번으로 가는 비용이 b이다. b를 기준으로 heap sorting 됨
    graph[a].append((b, c))


# Heap sort 사용 = O(e * log v)
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:    # 큐가 비어있지 않다면
        # 거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('unreached')
    else:
        print(distance[i])
