move = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}


def find(loc):
    x, y = loc
    if parent[x][y] != (x, y):
        parent[x][y] = find(parent[x][y])
    return parent[x][y]


def union(loc1, loc2):
    global answer
    ploc1 = find(loc1)
    ploc2 = find(loc2)

    # 이미 같은 집합이면 return
    if ploc1 == ploc2:
        return

    # rank 낮거나 같은 집합을 높은집합으로 합치기
    if rank[ploc1[0]][ploc1[1]] >= rank[ploc2[0]][ploc2[1]]:
        rank[ploc1[0]][ploc1[1]] += rank[ploc2[0]][ploc2[1]]
        answer -= 1
        parent[ploc2[0]][ploc2[1]] = parent[ploc1[0]][ploc1[1]]

    else:
        rank[ploc2[0]][ploc2[1]] += rank[ploc1[0]][ploc1[1]]
        answer -= 1
        parent[ploc1[0]][ploc1[1]] = parent[ploc2[0]][ploc2[1]]


# main
N, M = map(int, input().split())
graph = []
parent = [[(i, j) for j in range(M)] for i in range(N)]
rank = [[1] * M for _ in range(N)]
answer = N * M

for _ in range(N):
    graph.append(list(input().rstrip()))

for x in range(N):
    for y in range(M):
        cmd = graph[x][y]
        nx = x + move[cmd][0]
        ny = y + move[cmd][1]
        union((x, y), (nx, ny))

print(answer)

"""
1 3
RRL

정답: 1


10 10
DRDRRRRRRD
RDRUDUUUUL
URLDLRRRRD
RRRRLRDLUD
DDRLLDULUU
DRULLLRDUU
DULLDDDURU
URLDDDDUUL
DLRLRDUULL
RRULRUUURU

정답: 12


10 10
RRLLLLLRRL
UDDDULLDUU
RLURDULRUD
DULULLURRD
RUUURUDUDL
ULRUULLLLU
RDLLDDRLDD
DLRUULLRDL
UUUUUDULLD
URUULLRRRU

정답: 9
"""