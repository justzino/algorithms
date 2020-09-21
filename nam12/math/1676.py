# import sys

# N = int(sys.stdin.readline().rstrip())

# fac = 1
# for i in range(1, N+1):
#     fac *= i

# fac = str(fac)
# cnt = 0

# for i in range(len(fac)-1, -1, -1):
#     if fac[i] != '0':
#         break
#     if fac[i] == '0':
#         cnt += 1
# print(cnt)

import sys


N = int(sys.stdin.readline().rstrip())

fac = 1
for i in range(2, N+1):
    fac *= i

fac = list(str(fac))
cnt = 0

while fac:
    if fac[-1] != '0':
        print(cnt)
        break
    if fac[-1] == '0':
        fac.pop()
        cnt += 1
