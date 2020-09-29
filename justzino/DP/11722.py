from sys import stdin


N = int(stdin.readline())
seq = list(map(int, stdin.readline().split()))

dp = [[0 for _ in range(N)] for _ in range(N)]
longest_seq_len = 0

for i in range(N):
    longest_seq_len = max(longest_seq_len, dp[i][i])
    for j in range(i, N):
        if seq[i] > seq[j]:
            dp[i][j] = dp[i][i] + 1
            dp[j][j] = max(dp[i][j], dp[j][j])      # dp[j][j] 에 가장 큰 수 저장

longest_seq_len += 1        # 자기자신도 1 (즉, 초기값 1)
print(longest_seq_len)
