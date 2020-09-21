import sys

T = int(sys.stdin.readline())
N = [0] * T
for i in range(T):
    N[i] = int(sys.stdin.readline())

max_val = max(max(N), 3)
D = [0] * (max_val+1)
D[1] = 1
D[2] = 2
D[3] = 4
for i in range(4, max_val+1):
    D[i] = D[i-1]%1000000009 +  D[i-2]%1000000009 +  D[i-3]%1000000009

for i in N:
    print(D[i]%1000000009)

# 모듈러 쓰면 됨: https://ssu-gongdoli.tistory.com/38

# 메모리 초과
# T = int(sys.stdin.readline())
# N = [0] * T
# for i in range(T):
#     N[i] = int(sys.stdin.readline())

# max_val = max(max(N), 3)
# D = [0] * (max_val+1)
# D[1] = 1
# D[2] = 2
# D[3] = 4
# for i in range(4, max_val+1):
#     D[i] = D[i-1] +  D[i-2] +  D[i-3]

# for i in N:
#     print(D[i]%1000000009)