import sys
sys.setrecursionlimit(100000)

T = int(input())
parent = []
visited = []


def find(x):
    if visited[x]:
        return x
    visited[x] = True
    if parent[x] == x:
        return parent[x]
    return find(parent[x])


for _ in range(T):
    N = int(input())
    parent = [i for i in range(N + 1)]
    visited = [False for i in range(N + 1)]

    for _ in range(N - 1):
        a, b = map(int, input().split())
        parent[b] = a

    x, y = map(int, input().split())  # 공통조상 찾을 값
    find(x)
    root = find(y)
    print(root)
