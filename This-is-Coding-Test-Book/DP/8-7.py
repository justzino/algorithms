# 정수 n을 입력받기
n = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
dp = [0] * 1001
dp[1] = 1
dp[2] = 3

# DP 진행 (Bottom-up)
for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 796796

# 결과 출력
print(dp[n])

