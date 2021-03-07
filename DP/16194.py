import sys

n = int(sys.stdin.readline())
p = [0] + list(map(int, sys.stdin.readline().split()))

for i in range(1, n+1):
    _min = p[i]
    for j in range(1, i // 2 + 1):
        if _min > p[j] + p[i-j]:
            _min = p[j] + p[i-j]
        p[i] = _min
print(p[n])
