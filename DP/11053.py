import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
dp = [0 for i in range(n)]      # dp[i]까지의 최대 길이 저장

for i in range(n):
    for j in range(n):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))
