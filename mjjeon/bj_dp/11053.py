import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
cnt = [1] * N # 틀렸습니다. 초기화 다 1로...
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            cnt[i] = max(cnt[i], cnt[j] + 1)

print(max(cnt))


# 틀렸습니다 -> 초기화 다 1로 해주니 되었음.
# import sys

# N = int(sys.stdin.readline())
# A = list(map(int, sys.stdin.readline().split()))
# cnt = [0] * N
# cnt[0] = 1
# for i in range(N):
#     for j in range(i):
#         if A[i] > A[j]:
#             cnt[i] = max(cnt[i], cnt[j] + 1)

# print(max(cnt))