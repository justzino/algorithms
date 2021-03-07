# 바로 이전에 17298.오큰수 문제를 풀지 않았다면 풀지 못했을 문제.
import sys

n = int(sys.stdin.readline())

seq = list(map(int, sys.stdin.readline().split()))
result = [-1 for _ in range(n)]
stack = []

n_seq = {}
n_seq.setdefault(0)
for i in seq:
    n_seq.setdefault(i, 0)
    n_seq[i] += 1

for i in range(n):
    try:
        while n_seq[seq[stack[-1]]] < n_seq[seq[i]]:
            result[stack.pop()] = seq[i]
    except:
        pass

    stack.append(i)

for i in range(n):
    print(result[i], end=' ')