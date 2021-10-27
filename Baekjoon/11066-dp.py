import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    pages = [0] + list(map(int, input().split()))
    dp = [[0 for j in range(N+1)] for i in range(N+1)]
    sums = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        sums[i] = sums[i-1] + pages[i]

    for j in range(2, N+1):
        for i in range(j-1, 0, -1):
            values = [dp[i][k] + dp[k+1][j]for k in range(i, j)]
            dp[i][j] = min(values) + sums[j]-sums[i-1]
    print(dp[1][N])