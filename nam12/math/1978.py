import sys

N = int(sys.stdin.readline().rstrip())
ans = 0

x = list(map(int, input().split()))

for i in range(N):
    cnt = 0
    for idx in range(1, x[i]+1):
        if cnt > 2:
            break
        if x[i] % idx == 0:
            cnt += 1
    if cnt == 2:
        ans += 1
print(ans)
