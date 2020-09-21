import sys

N = int(sys.stdin.readline())
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
for n in range(N):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(n+1):
        dp[n][i] = max(dp[n-1][i-1], dp[n-1][i]) + line[i]
print(max(dp[N-1]))