def fac(n):
    if n == 0 or N == 1:
        return 1
    else:
        r = 1
        for i in range(1, n+1):
            r *= i
    return r


def fac2(n, m):     # nPm
    r = 1
    for i in range(n-m+1, n+1):
        r *= i
    return r


def combination(n, m):
    if m == 0:              # nC0 == 1
        return 1
    elif n < 2 * m:         # n-m < m 인 경우
        return fac2(n, n-m) // fac(n-m)
    return fac2(n, m) // fac(m)


N, M = map(int, input().split())
cnt = 0
result = combination(N, M)
print(result)

while result % 10 == 0:
    cnt += 1
    result = result // 10
print(cnt)
