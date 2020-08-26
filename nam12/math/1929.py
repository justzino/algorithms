import sys
import math

M, N = map(int, (sys.stdin.readline().rstrip().split()))

for i in range(M, N+1):

    check = True

    n = int(math.sqrt(i))
    for j in range(2, n+1):
        if i % j == 0:
            check = False
            break
    if check:
        print(i)
