# 핵심 아이디어 : MST 만든 다음에 가장 cost 큰 간선 제거
import sys
input = sys.stdin.readline

def find_root(parent, x):
    if parent[x] != x:
        parent[x] = find_root(parent, parent[x])
    return parent[x]


def union_set(parent, a, b):
    a = find_root(parent, a)
    b = find_root(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
paths = []
result = 0
longest_edge_cost = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    paths.append((cost, a, b))

paths.sort()

parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i


for edge in paths:
    cost, a, b = edge
    if find_root(parent, a) != find_root(parent, b):
        union_set(parent, a, b)
        longest_edge_cost = cost
        result += cost

print(result - longest_edge_cost)

# 7 12
# 1 2 3
# 1 3 2
# 3 2 1
# 2 5 2
# 3 4 4
# 7 3 6
# 5 1 5
# 1 6 2
# 6 4 1
# 6 5 3
# 4 5 3
# 6 7 4
