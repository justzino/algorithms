from itertools import combinations

n = int(input())
graph = []

teachers = []
empty = []


for i in range(n):
    graph.append(list(input().split()))
    for j in range(n):
        if graph[i][j] == 'T':
            teachers.append((i, j))
        elif graph[i][j] == 'X':
            empty.append((i, j))


def watch(x, y, direction):
    # 아래
    if direction == 0:
        while x < n:
            if graph[x][y] == 'O':  # 장애물이 있는 경우
                return True
            elif graph[x][y] == 'S':    # 학생이 있는 경우
                return False
            x += 1
    # 오른쪽
    elif direction == 1:
        while y < n:
            if graph[x][y] == 'O':  # 장애물이 있는 경우
                return True
            elif graph[x][y] == 'S':  # 학생이 있는 경우
                return False
            y += 1
    # 위쪽
    elif direction == 2:
        while x >= 0:
            if graph[x][y] == 'O':  # 장애물이 있는 경우
                return True
            elif graph[x][y] == 'S':  # 학생이 있는 경우
                return False
            x -= 1
    # 왼쪽
    else:
        while y >= 0:
            if graph[x][y] == 'O':  # 장애물이 있는 경우
                return True
            elif graph[x][y] == 'S':  # 학생이 있는 경우
                return False
            y -= 1

    return True     # 아무것도 없는 경우


def simulation():
    # 모든 선생님들에 대해 watch
    for teacher in teachers:
        x, y = teacher[0], teacher[1]
        # 4방향에 대해 watch
        for i in range(4):
            # 학생 보이면 False
            if not watch(x, y, i):
                return False

    # 학생 안보이면 True
    return True


find_flag = False

# 빈 공간에서 3개 위치 뽑기 -> 장애물 설치 시뮬레이션
for case in combinations(empty, 3):
    # 각 경우 시뮬레이션 시작 -> 감시 피할 수 있으면 True, 없으면 False
    for x, y in case:
        graph[x][y] = 'O'

    # 학생 안보이면 True
    if simulation():
        print(graph)
        find_flag = True
        break

    for x, y in case:
        graph[x][y] = 'X'

if find_flag:
    print('YES')
else:
    print('NO')

"""
3 <= N <= 6
객체: 선생님, 학생, 장애물
장애물 3개 설치
T <= 5, S <= 30
"""