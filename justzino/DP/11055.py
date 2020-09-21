from sys import stdin

N = int(stdin.readline())

dp = [[0 for _ in range(N)] for _ in range(N)]
seq = list(map(int, stdin.readline().split()))
_max = 0

for i in range(N):
    dp[i][i] = seq[i]
    for j in range(i+1):
        if seq[i] > seq[j]:
            dp[i][j] = seq[i] + dp[j][j]
            dp[i][i] = max(dp[i][j], dp[i][i])
    _max = max(_max, dp[i][i])
print(_max)
