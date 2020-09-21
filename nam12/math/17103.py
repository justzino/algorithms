import sys
import math

MAX = 1000000
prime = [True for _ in range(MAX + 10)]

for i in range(2, int(math.sqrt(MAX)+1)):
    if prime[i] == True:
        for j in range(2*i, MAX+1, i):
            prime[j] = False
# 1도 True로 되어있음에 주의

t = int(sys.stdin.readline().rstrip())

for i in range(t):

    partition = 0

    N = int(sys.stdin.readline().rstrip())

    for i in range(2, int(N/2)+1, 1):
        if prime[i] == True:
            if prime[N-i] == True:
                partition += 1
    print(partition)
