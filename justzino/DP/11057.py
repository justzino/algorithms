N = int(input())

dp = [[0 for _ in range(10)] for _ in range(N+1)]
dp[1] = [1 for _ in range(10)]

for n in range(2, N+1):
    for i in range(10):
        for j in range(i+1):
            dp[n][i] += dp[n-1][j]
        dp[n][i] %= 10007
print(sum(dp[N]) % 10007)
