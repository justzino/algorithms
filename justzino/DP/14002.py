import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(n)]      # dp[i]까지의 최대 길이 저장
dp2 = [0 for _ in range(n)]     # dp[i] 이전 수열의 인덱스
max_len = 0
max_idx = 0

for i in range(n):
    for j in range(n):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
            dp2[i] = j
    dp[i] += 1
    if max_len < dp[i]:
        max_len = dp[i]
        max_idx = i

max_seq = [max_idx]
while dp2[max_idx] < max_idx:
    max_seq.append(dp2[max_idx])
    max_idx = dp2[max_idx]

print(max_len)
while max_seq:
    print(a[max_seq.pop()], end=' ')
