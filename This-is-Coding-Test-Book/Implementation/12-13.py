from itertools import combinations
import copy

n, total = map(int, input().split())
MAXIMUM = 1e9
house = []
chicken = []


# 두 위치간 거리 구하기
def cal_distance(locate1, locate2):
    return abs(locate1[0] - locate2[0]) + abs(locate1[1] - locate2[1])


# 특정 집 좌표에서 chicken 집까지의 거리 list 구하기
def distance_chicken(house_locate):
    distance = []
    for x, y in chicken:
        distance.append(cal_distance(house_locate, (x, y)))
    return distance


for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            house.append((i+1, j+1))
        elif data[j] == 2:
            chicken.append((i+1, j+1))

n_house = len(house)
n_chicken = len(chicken)
matrix = [[0] for _ in range(n_house)]

# 모든 house x chicken 거리 matrix 에 저장
for i in range(n_house):
    matrix[i] = distance_chicken(house[i])


# 임의의 n_chicken - total 개 chicken 을 고른 후 해당 치킨집까지의 거리는 무한으로 만듬
data = [i for i in range(n_chicken)]
result = []

selects = list(combinations(data, n_chicken - total))
for x in selects:
    copy_matrix = copy.deepcopy(matrix)
    mins = []
    # total 개의 chicken 집을 남겨두고 나머지 치킨집까지의 거리는 MAXIMUM
    for j in x:
        for i in range(n_house):
            copy_matrix[i][j] = MAXIMUM

    for i in range(n_house):
        # 각 house의 치킨 거리
        mins.append(min(copy_matrix[i]))

    result.append(sum(mins))

# 도시의 치킨 거리 list 의 최소값 출력
print(min(result))
