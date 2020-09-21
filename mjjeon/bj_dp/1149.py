import sys
N = int(sys.stdin.readline())
D = [[0,0,0] for i in range(N)]
result = 0
for i in range(N):
    house = list(map(int, sys.stdin.readline().split()))
    D[i][0] = min(D[i-1][1], D[i-1][2]) + house[0]
    D[i][1] = min(D[i-1][0], D[i-1][2]) + house[1]
    D[i][2] = min(D[i-1][0], D[i-1][1]) + house[2]

print(min(D[N-1]))


# 틀렸습니다

# import sys
# N = int(sys.stdin.readline())
# D = [0] * N
# house = []
# result = 0
# for i in range(N):
#     house.append(list(map(int, sys.stdin.readline().split())))
    
#     min_value = min(house[i])
#     min_idx = house[i].index(min_value)
#     if D[i-1] == min_idx and i != 0:
#         house[i][min_idx] = 1001
#         min_value = min(house[i])
#         min_idx = house[i].index(min_value)
    
#     D[i] = min_idx
#     result += min_value
    
# print(result)