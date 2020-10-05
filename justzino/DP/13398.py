from sys import stdin

N = int(stdin.readline())
seq = list(map(int, stdin.readline().split()))

dp1 = seq[:]
dp2 = seq[:]
max_num = -1001

for i in range(1, N):
    if dp1[i-1] + seq[i] > seq[i]:
        dp1[i] = dp1[i-1] + seq[i]


for i in range(N-2, -1, -1):
    if dp2[i+1] + seq[i] > seq[i]:
        dp2[i] = dp2[i+1] + seq[i]

dp1 += [0, 0]
dp2 += [0, 0]

for i in range(N):
    max_num = max(max_num, dp1[i] + dp2[i+1], dp1[i] + dp2[i+2], dp1[i], dp2[i])

print(max_num)

# 메모리 초과 뿐만 아니라 최대값 구하는 것도 잘못됨.
# dp = [[0 for _ in range(N)] for _ in range(N)]
# max_dp = [0 for _ in range(N)]
# max_num = 0
#
# for i in range(N):
#     if seq[i] > dp[i][i]:   # 최대값(대각선 값) 갱신, 밑에 값들도 계산
#         dp[i][i] = seq[i]
#         for j in range(i+1, N):
#             dp[i][j] = dp[i][j - 1] + seq[j]
#             dp[j][j] = max(dp[i][j], dp[j][j])
#     max_dp[i] = dp[i][i]
#     dp[i][i] = 0
#
# for i in range(N-1, -1, -1):
#     if seq[i] > dp[i][i]:   # 최대값(대각선 값) 갱신, 위에 값들도 계산
#         dp[i][i] = seq[i]
#         for j in range(i-1, -1, -1):
#             dp[i][j] = dp[i][j-1] + seq[j]
#             dp[j][j] = max(dp[i][j], dp[j][j])
#
# for i in range(N):
#     max_num = max(max_num, max_dp[i] + dp[i][i])
#
# print(max_num)