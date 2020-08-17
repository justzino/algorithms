# 런타임 에러
import sys

n = int(sys.stdin.readline())

stack = []
seq = []
idx = 0
result = []
for _ in range(n):
    seq = int(sys.stdin.readline())

for i in range(1, n+1):
    stack.append(i)
    result.append('+')

    while seq[idx] == stack[-1]:
        stack.pop()
        result.append('-')
        idx += 1

if stack:
    print('NO')
else:
    for c in result:
        print(c)
