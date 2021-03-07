import sys

N = int(sys.stdin.readline())
dp = [[0, 0, 0] for _ in range(1001)]

for n in range(1, N+1):
    dp[n] = list(map(int, sys.stdin.readline().split()))
    dp[n][0] = min(dp[n-1][1], dp[n-1][2]) + dp[n][0]
    dp[n][1] = min(dp[n - 1][0], dp[n - 1][2]) + dp[n][1]
    dp[n][2] = min(dp[n - 1][0], dp[n - 1][1]) + dp[n][2]
print(min(dp[N]))
