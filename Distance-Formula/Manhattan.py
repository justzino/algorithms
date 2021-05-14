# 맨하탄 거리 구하는 알고리즘
def manhattan_distance(p1, p2):
    distance = 0
    for i in range(len(p1)):
        distance += abs(p1[i] - p2[i])
    return distance


print(manhattan_distance([5, 4, 3], [1, 7, 9]))
