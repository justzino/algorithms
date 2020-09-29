from sys import stdin

N = int(stdin.readline())
seq = list(map(int, stdin.readline().split()))

increasing_dp = [[0 for _ in range(N)] for _ in range(N)]
decreasing_dp = [[0 for _ in range(N)] for _ in range(N)]
longest_seq_len = 0

for i in range(N):
    for j in range(i, N):
        if seq[i] < seq[j]:
            increasing_dp[i][j] = increasing_dp[i][i] + 1
            increasing_dp[j][j] = max(increasing_dp[j][j], increasing_dp[i][j])

for i in range(N-1, -1, -1):
    for j in range(i, -1, -1):
        if seq[j] > seq[i]:
            decreasing_dp[i][j] = decreasing_dp[i][i] + 1
            decreasing_dp[j][j] = max(decreasing_dp[j][j], decreasing_dp[i][j])

for i in range(N):
    longest_seq_len = max(longest_seq_len, increasing_dp[i][i] + decreasing_dp[i][i])
longest_seq_len += 1

print(longest_seq_len)
