import sys


def gcd(a, b):
    while(b != 0):
        r = a % b
        a = b
        b = r
    return a


def gccd(a, b):
    return int((a*b)/gcd(a, b))


A, B = map(int, sys.stdin.readline().rstrip().split())

print(gcd(A, B))
print(gccd(A, B))
