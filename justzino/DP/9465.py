import sys

T = int(sys.stdin.readline())

# dp = [[0 for _ in range(100001)] for _ in range(2)]

for _ in range(T):
    N = int(sys.stdin.readline())
    dp = [[0 for _ in range(N)] for _ in range(2)]
    dp[0] = list(map(int, sys.stdin.readline().split())) + [0]      # [0] 더해준 이유 : dp[][i-2]를 더할때 i=1일때 생각.
    dp[1] = list(map(int, sys.stdin.readline().split())) + [0]

    for i in range(1, N):
        dp[0][i] += max(dp[1][i-1], dp[1][i-2])
        dp[1][i] += max(dp[0][i-1], dp[0][i-2])
    print(max(dp[0][N-1], dp[1][N-1]))
