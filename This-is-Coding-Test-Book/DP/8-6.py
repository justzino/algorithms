n = int(input())
# 모든 식량 정보 입력받기
foods = list(map(int, input().split()))

# 앞서 계산된 결과를 젖ㅇ하기 위한 DP 테이블 초기화
dp = [0] * n
dp[0] = foods[0]
dp[1] = foods[1]

# DP 진행 (Bottom-up)
for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + foods[i])

print(dp[n-1])
