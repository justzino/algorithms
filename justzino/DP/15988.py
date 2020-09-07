import sys

dp = [[0]*3 for i in range(1000001)]
dp[1] = [1, 0, 0]   # 1, 2, 3이 처음 오는 경우 순
dp[2] = [1, 1, 0]
dp[3] = [2, 1, 1]

for i in range(4, 1000001):
    dp[i][0] = sum(dp[i-1]) % 1000000009
    dp[i][1] = sum(dp[i-2]) % 1000000009
    dp[i][2] = sum(dp[i-3]) % 1000000009

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(sum(dp[n]) % 1000000009)