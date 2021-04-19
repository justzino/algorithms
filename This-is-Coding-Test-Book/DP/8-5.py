# 정수 X 입력받기
n = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
dp = [0] * 30001

# DP 진행 (Bottom-up)
for i in range(6, n + 1):
    # 현재의 수에서 1을 빼는 경우
    dp[i] = dp[i - 1] + 1
    # 현재의 수가 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        dp[i] = min(dp[i // 5] + 1, dp[i])
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i // 3] + 1, dp[i])
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i // 2] + 1, dp[i])

print(dp[n])
