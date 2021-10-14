a, b, c = map(int, input().split())


# (a ** b) % c
def func(a, b, c):
    if b == 1:
        return a % c
    val = func(a, b // 2, c)
    val = val * val % c
    if b % 2 == 0:
        return val
    else:
        return val * a % c


print(func(a, b, c))