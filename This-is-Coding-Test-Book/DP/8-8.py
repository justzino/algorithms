# 정수 N, M을 입력 받기
n, m = map(int, input().split())
# 계산된 결과를 저장하기 위한 DP 테이블 초기화
dp = [10001] * 10001

# N 개의 화폐 단위 정보를 입력받기 -> 화폐의 dp = 1
for _ in range(n):
    coin = int(input())
    dp[coin] = 1

# DP 진행 (Bottom-up)
for i in range(1, m + 1):
    # i = j + (i-j)
    for j in range(1, i // 2 + 1):
        dp[i] = min(dp[i], dp[j] + dp[i-j])

if dp[m] < 10001:
    print(dp[m])
else:
    print(-1)
