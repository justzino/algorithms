def dfs(graph, v, visited):
    visited[v] = True
    cnt = 1

    for node in graph[v]:
        if not visited[node]:
            cnt += dfs(graph, node, visited)

    return cnt


# 백트래킹
def simulate(graph, wire, n):
    a, b = wire
    visited = [False] * (n + 1)

    # 없애고 시뮬레이션
    graph[a].remove(b)
    graph[b].remove(a)

    cnt_a = dfs(graph, a, visited)
    cnt_b = dfs(graph, b, visited)
    gap = abs(cnt_a - cnt_b)

    # 되돌리기
    graph[a].append(b)
    graph[b].append(a)

    return gap


def solution(n, wires):
    graph = [[] for _ in range(n + 1)]

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    gap = 1000
    for wire in wires:
        gap = min(gap, simulate(graph, wire, n))

    return gap