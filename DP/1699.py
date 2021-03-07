# 12 = 4, 4, 4 / 9, 1, 1, 1
# 13 = 4, 4, 4, 1 / 9, 4
# 18 = 9, 9 / 16, 1, 1, 1
n = int(input())
dp = [0 for i in range(n+1)]    # 항의 개수

for i in range(1, n+1):
    dp[i] = i
    for j in range(1, i):
        if j*j > i:
            break
        if dp[i] > dp[i - j * j] + 1:
            dp[i] = dp[i - j * j] + 1
print(dp[n])
