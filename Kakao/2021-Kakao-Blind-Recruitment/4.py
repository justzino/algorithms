INF = int(1e9)


def solution(n, s, a, b, fares):
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기자신 0으로 초기화
    for i in range(1, n + 1):
        graph[i][i] = 0

    # 한번에 갈수 있는 거리 초기화
    for x, y, dist in fares:
        graph[x][y] = dist
        graph[y][x] = dist

    # a->b까지 가는데 x를 거쳐가는 거리 계산
    for k in range(1, n + 1):
        for x in range(1, n + 1):
            for y in range(x, n + 1):
                dist = min(graph[x][y], graph[x][k] + graph[k][y])
                graph[x][y] = dist
                graph[y][x] = dist

    # s -> x -> a,b 경우의 수 합 중 가장 작은 경우 구하기
    result = INF
    node = 0
    for x in range(1, n + 1):
        dist = min(result, graph[s][x] + graph[x][a] + graph[x][b])
        if result > dist:
            result = dist
            node = x

    return result