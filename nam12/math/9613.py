import sys


def gcd(A, B):
    a = max(A, B)
    b = min(A, B)
    temp = 0
    while temp != 0:
        temp = a % b
        a = b
        b = temp
    return a


t = int(sys.stdin.readline().rstrip())

for i in range(t):

    n = int(sys.stdin.readline().rstrip())
    arr = list(map(int, (sys.stdin.readline().rstrip().split())))

    sum = 0
    for i in range(n):
        for j in range(1, n):
            print(gcd(arr[i], arr[j]))
            sum += gcd(arr[i], arr[j])
    print(sum)
