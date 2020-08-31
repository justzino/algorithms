import sys


def gcd(A, B):
    a = max(A, B)
    b = min(A, B)
    while(b != 0):
        r = a % b
        a = b
        b = r
    return a


def gccd(a, b):
    return int((a*b)/gcd(a, b))


N = int(sys.stdin.readline().rstrip())

for i in range(N):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print(gccd(A, B))
