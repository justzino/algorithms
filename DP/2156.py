import sys

N = int(sys.stdin.readline())
dp = [[0, 0, 0] for _ in range(N+1)]

for i in range(1, N+1):
    now = int(sys.stdin.readline())
    dp[i][0] = max(dp[i-1])       # i번째 포도주 안마시는 경우
    dp[i][1] = dp[i-1][0] + now   # i번째 포도주 마셔서 연속 처음
    dp[i][2] = dp[i-1][1] + now   # i번째 포도줌 마셔서 연속 두번
print(max(dp[N]))
