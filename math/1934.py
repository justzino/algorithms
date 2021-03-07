import sys


def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)


def lcm(x, y):
    return int(x * y / gcd(x, y))


n = int(sys.stdin.readline())
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(lcm(a, b))