import sys
import itertools


def gcd(A, B):
    a = max(A, B)
    b = min(A, B)

    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


t = int(sys.stdin.readline().rstrip())

for i in range(t):

    arr = list(map(int, (sys.stdin.readline().rstrip().split())))

    n = arr[0]
    sum = 0

    for i in range(1, n):
        for j in range(i+1, n+1):
            sum += gcd(arr[i], arr[j])
    print(sum)
