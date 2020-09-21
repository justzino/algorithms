import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
max_value = 0
P.insert(0, 0)
D = [0] * 1001

# 1 ~ N장까지 사는 것까지 고려해야하기 때문.
for i in range(1, N+1):
    for j in range(1, i+1):
        D[i] = max(D[i], P[j] + D[i-j])

print(D[N])

# 틀렸습니다.
# import sys

# N = int(sys.stdin.readline())
# P = list(map(int, sys.stdin.readline().split()))
# max_value = 0
# P.insert(0, 0)

# for i in range(1, N+1):
    
#     # 같은 카드
#     if N%(i) == 0:
#         value = P[i] * N//(i)
#         if max_value < value:
#             max_value = value
    
#     # N - i, i 카드
#     value = P[i] + P[N-i]

#     if max_value < value:
#         max_value = value

# print(max_value)