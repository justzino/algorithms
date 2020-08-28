import sys


def fac(n):

    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


N, M = map(int, sys.stdin.readline().rstrip().split())

combination = int(fac(N)/(fac(N-M)*fac(M)))

c = list(str(combination))

cnt = 0
while c:

    if c[-1] != '0':
        print(cnt)
        break
    else:
        cnt += 1
        c.pop()
