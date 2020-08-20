# 시간 초과
# import sys
#
# n = int(sys.stdin.readline())
# seq = list(map(int, sys.stdin.readline().split()))
# result = [-1 for _ in range(n)]
#
# for i in range(len(seq)):
#     for j in seq[i:]:
#         if seq[i] < j:
#             result[i] = j
#             break
#
# for i in result:
#     print(i, end=' ')

# 답 찾아봄
import sys

n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
result = [-1 for _ in range(n)]
stack = []

for i in range(n):
    try:
        while seq[stack[-1]] < seq[i]:
            result[stack.pop()] = seq[i]
    except:
        pass

    stack.append(i)

for i in range(n):
    print(result[i], end=' ')