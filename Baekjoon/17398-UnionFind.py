import sys
input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])     # 경로 압축 (path compression)
    return parent[x]


def union(x, y):
    px = find(x)
    py = find(y)

    # 분리 후에도 연결 되어 있으면 비용 0
    if px == py:
        return 0
    # 연결 끊기면 비용 계산
    cost = rank[px] * rank[py]   # 비용 계산 해서 리턴
    if rank[px] < rank[py]:     # rank compression
        parent[py] = px
        rank[px] += rank[py]
    else:
        parent[px] = py
        rank[py] += rank[px]

    return cost


# main
N, M, Q = map(int, input().split())
edges = []
removes = []
connected = [True] * M

parent = [i for i in range(N + 1)]
rank = [1 for i in range(N + 1)]  # parent 에 속해 있는 노드 개수 저장

for i in range(M):
    a, b = map(int, input().split())
    edges.append((a, b))

for _ in range(Q):
    idx = int(input())-1
    removes.append(idx)
    connected[idx] = False

# 제거된 거 제외하고 전부 연결
for i in range(M):
    if connected[i]:
        union(edges[i][0], edges[i][1])

answer = 0
# 제거 역순으로 연결 하며 비용 계산
while removes:
    i = removes.pop()
    a, b = edges[i]
    # 연결하기
    answer += union(a, b)

print(answer)
