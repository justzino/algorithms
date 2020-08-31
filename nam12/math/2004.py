import sys


def fac(n):

    fact = 1
    for i in range(2, n+1):
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
# 위 처럼 하니깐 시간초과 떴음.


def Get_number(n, m):  # 1번 째 인자는 구하고 싶은 숫자 , 2번째는 5, 2

    cnt = 0
    while n != 0:
        n = n//m
        cnt += n
    return cnt


N, M = map(int, sys.stdin.readline().rstrip().split())

a = Get_number(N, 5) - Get_number(M, 5) - Get_number(N-M, 5)
b = Get_number(N, 2) - Get_number(M, 2) - Get_number(N-M, 2)

print(min(a, b))
