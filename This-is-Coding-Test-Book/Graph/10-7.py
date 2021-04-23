# 특정 원소가 속한 집합을 찾기
def find_root(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 떄까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_root(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_set(parent, a, b):
    a = find_root(parent, a)
    b = find_root(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
data = []

for _ in range(m):
    data.append(list(map(int, input().split())))

# 부모 테이블 자기자신으로 초기화
parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i

# 각 연산 하나씩 확인
for op in data:
    # 합집합인 경우
    if op[0] == 0:
        union_set(parent, op[1], op[2])
    # 찾기 연산인 경우
    elif op[0] == 1:
        if find_root(parent, op[1]) == find_root(parent, op[2]):
            print("YES")
        else:
            print("NO")

# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1
