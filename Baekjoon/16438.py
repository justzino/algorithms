N = int(input())
result = [[] for _ in range(7)]
TEAM = ['A', 'B']


def divide_conquer(n, day, flag):
    if day >= 7:
        return
    if n <= 1:
        if len(result[day]) == N:
            return
        result[day] += TEAM[flag]
        divide_conquer(1, day + 1, flag)

    else:
        left = ['A'] * (n // 2)
        right = ['B'] * (n - n // 2)
        result[day] += (left + right)

        divide_conquer(len(left), day + 1, 0)
        divide_conquer(len(right), day + 1, 1)


divide_conquer(N, 0, 0)
# 전부 싸웠는지 판단용
# graph = [set() for _ in range(N)]
# for i in range(7):
#     team1, team2 = [], []
#     for j in range(N):
#         team1.append(j) if result[i][j] == 'A' else team2.append(j)
#     for x in team1:
#         graph[x].update(team2)
#     for y in team2:
#         graph[y].update(team1)
#
# n_graph = []
# for s in graph:
#     n_graph.append(len(s))
#
# print(n_graph)
answer = ""
for line in result:
    print("".join(line))