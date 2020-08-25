import sys

def GCD(a, b):
    if a % b == 0:
        return b
    else:
        return GCD(b, a % b)

n, s = map(int, sys.stdin.readline().split())
sisters = list(map(int, sys.stdin.readline().split()))

values = [abs(i - s) for i in sisters]

for i in range(n - 1):
    values[i+1] = GCD(values[i], values[i+1])

print(values[-1]) 