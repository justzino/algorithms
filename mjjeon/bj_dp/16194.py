import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
max_value = 0
P.insert(0, 0)
D = [0] * 1001

# 1 ~ N장까지 사는 것까지 고려해야하기 때문.
for i in range(1, N+1):
    for j in range(1, i+1):
        if D[i] == 0:
            D[i] = P[j] + D[i-j]
        D[i] = min(D[i], P[j] + D[i-j])

print(D[N])

# 11052 에서 조금 변형해서.. 최소값이므로 0일 때만 처리부분 넣어줌.