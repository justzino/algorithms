import sys
input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    px = find(x)
    py = find(y)

    if rank[px] < rank[py]:
        parent[px] = py
        rank[py] += rank[px]
    else:
        parent[py] = px
        rank[px] += rank[py]


# main
n, m = map(int, input().split())
parent = [i for i in range(n+1)]
rank = [1 for i in range(n+1)]

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:     # union
        union(a, b)

    else:       # 같은 집합에 속해있는지 확인
        pa = find(a)
        pb = find(b)

        if pa == pb:
            print('YES')
        else:
            print('NO')
