from sys import stdin

N = int(stdin.readline())
costs = [[0, 0, 0] for _ in range(N)]
for i in range(N):
    costs[i] = list(map(int, stdin.readline().split()))

dp = [[0, 0, 0] for _ in range(N)]
dp_startR = 0
dp_startG = 0
dp_startB = 0

# 1번 집 Red 선택
dp[0] = [costs[0][0], 10000, 10000]
for i in range(1, N):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]
dp_startR = min(dp[N - 1][1], dp[N - 1][2])

# 1번 집 Green 선택
dp[0] = [10000, costs[0][1], 10000]
for i in range(1, N):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]
dp_startG = min(dp[N - 1][0], dp[N - 1][2])

# 1번 집 Blue 선택
dp[0] = [10000, 10000, costs[0][2]]
for i in range(1, N):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]
dp_startB = min(dp[N - 1][0], dp[N - 1][1])

print(min(dp_startR, dp_startG, dp_startB))
