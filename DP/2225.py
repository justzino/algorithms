N, K = map(int, input().split())

dp = [[0] * 201 for i in range(201)]

for i in range(201):
    dp[0][i] = 1

for k in range(1, K + 1):
    for n in range(1, N + 1):
        for i in range(n+1):
            dp[n][k] += dp[i][k-1]
        dp[n][k] %= 1000000000

print(dp[N][K])
