# dp[n] = dp[n-2] * 3 + (dp[n-4] + dp[n-6] + dp[n-8] + ... + dp[2]) * 2 + 2
# N < 2일때 dp[2] = 3 해버려서 런타임 에러 남
N = int(input())

dp = [0 for _ in range(N+1)]
sum_dp = 0

if N > 1:
    dp[2] = 3
    for i in range(4, N+1, 2):
        dp[i] = dp[i-2] * 3 + sum_dp * 2 + 2
        sum_dp += dp[i-2]

print(dp[N])
