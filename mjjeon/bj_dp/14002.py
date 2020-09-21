import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
cnt = [1] * N 
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            cnt[i] = max(cnt[i], cnt[j] + 1)

max_val = max(cnt)
print(max_val)

idx = cnt.index(max_val)

value = 0
values = []

while max_val >= 1:
    if cnt[idx] == max_val:
        values.append(A[idx])
        max_val -= 1
    idx -= 1


print(*reversed(values))


# 틀렸습니다
# 반례: https://takeknowledge.tistory.com/109 
# 7
# 1 6 2 4 5 3 7
# import sys

# N = int(sys.stdin.readline())
# A = list(map(int, sys.stdin.readline().split()))
# B = set()
# cnt = [1] * N 
# for i in range(N):
#     for j in range(i):
#         if A[i] > A[j]:
#             cnt[i] = max(cnt[i], cnt[j] + 1)
#             B.update([A[j]])
#             B.update([A[i]])

# print(max(cnt))
# print(*sorted(B))

# 틀렸습니다 : 모르겠음 위 반례도 고침, 도저히?
# 구글링해서 방법대로 함: https://hooongs.tistory.com/225
# import sys

# N = int(sys.stdin.readline())
# A = list(map(int, sys.stdin.readline().split()))
# cnt = [1] * N 
# for i in range(N):
#     for j in range(i):
#         if A[i] > A[j]:
#             cnt[i] = max(cnt[i], cnt[j] + 1)

# max_val = max(cnt)
# print(max_val)

# value = 0
# values = []
# for i in range(N):
#     if value < cnt[i]:
#         value = cnt[i]
#         values.append(A[i])
#     elif value == cnt[i] and values[-1] > A[i]:
#         values[-1] = A[i]
# print(*values)
