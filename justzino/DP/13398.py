from sys import stdin

N = int(stdin.readline())
seq = list(map(int, stdin.readline().split()))

dp1 = [[0 for _ in range(N)] for _ in range(N)]
dp2 = [[0 for _ in range(N)] for _ in range(N)]
max_num = 0

for i in range(N):
    if seq[i] > dp1[i][i]:   # 최대값(대각선 값) 갱신, 밑에 값들도 계산
        for j in range(i+1, N):
            dp1[i][i] = seq[i]
            dp1[i][j] = dp1[i][j-1] + seq[j]
            dp1[j][j] = max(dp1[i][j], dp1[j][j])

for i in range(N-1, -1, -1):
    if seq[i] > dp2[i][i]:   # 최대값(대각선 값) 갱신, 위에 값들도 계산
        for j in range(i-1, -1, -1):
            dp2[i][i] = seq[i]
            dp2[i][j] = dp2[i][j-1] + seq[j]
            dp2[j][j] = max(dp2[i][j], dp2[j][j])

for i in range(N):
    max_num = max(max_num, dp1[i][i] + dp2[i][i])

print(max_num)
