import sys


n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))

prime = [2, ]
check = 3
n_prime = 0

for i in range(n):
    for j in range(x[i]):

