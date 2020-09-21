import sys
N = int(sys.stdin.readline())
D = [[0, 0, 0] for i in range(N+1)]
D[0] = [1, 1, 1] # 없는 경우, 왼쪽, 오른쪽
D[1] = [1, 1, 1]
for i in range(2, N+1):
    D[i][0] = (D[i-1][0] + D[i-1][1] + D[i-1][2]) % 9901
    D[i][1] = (D[i-1][0] + D[i-1][2]) % 9901
    D[i][2] = (D[i-1][0] + D[i-1][1]) % 9901

print(sum(D[N]) % 9901)

# 메모리 초과
# import sys
# N = int(sys.stdin.readline())
# D = [[0, 0, 0] for i in range(N+1)]
# D[0] = [1, 1, 1] # 없는 경우, 왼쪽, 오른쪽
# D[1] = [1, 1, 1]
# for i in range(2, N+1):
#     D[i][0] = D[i-1][0] + D[i-1][1] + D[i-1][2]
#     D[i][1] = D[i-1][0] + D[i-1][2]
#     D[i][2] = D[i-1][0] + D[i-1][1]

# print(sum(D[N]))
