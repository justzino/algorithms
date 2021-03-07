# import sys
#
# n = int(sys.stdin.readline())
# seq = list(map(int, sys.stdin.readline().split()))
#
# tmp, tmp2, _max = 0, 0, 0
#
# for i in seq:
#     if i < 0:
#         if tmp + i < 0:
#             _max = max(tmp, tmp2, _max)
#             tmp, tmp2 = 0, 0
#             continue
#         if tmp2 > tmp:
#             _max = max(tmp2, _max)
#         tmp2 = tmp
#         tmp += i
#
#     else:
#         tmp += i
#         if tmp > _max:
#             _max = tmp
#
#
# print(_max)

import sys

n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
tmp = [0 for _ in range(n)]
result = -1001

for i in range(n):
    tmp[i] = max(tmp[i - 1] + seq[i], seq[i])
    result = max(result, tmp[i])

print(result)

