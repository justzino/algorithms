# 정수 N, M을 입력 받기
n, m = map(int, input().split())
# N개의 화폐 단위 정보를 입력받기
coins = []
for _ in range(n):
    coins.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
dp = [10001] * 10001

# DP 진행 (Bottom-up)
dp[0] = 0
for coin in coins:
    for i in range(coin, m + 1):
        if dp[i - coin] != 10001:    # (i-k)원을 만드는 방법이 존재하는 경우
            dp[i] = min(dp[i], dp[i - coin] + 1)

# 계산된 결과 출력
if dp[m] == 10001:      # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(dp[m])
