import sys

n, k = map(int, sys.stdin.readline().rstrip().split(' '))

seq = [i for i in range(1, n+1)]
result = []
cnt_result = 0
idx = 0

while cnt_result < n:
    if idx % k == k-1:
        result.append(seq[idx])
        cnt_result += 1
    else:
        seq.append(seq[idx])
    idx += 1

print('<', end='')
for i in result[:n-1]:
    print(i, end=', ')
print('{}>'.format(result[-1]), end='')