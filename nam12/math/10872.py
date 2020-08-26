import sys

N = int(sys.stdin.readline().rstrip())

fac = 1
for i in range(1, N+1):
    fac *= i
print(fac)
