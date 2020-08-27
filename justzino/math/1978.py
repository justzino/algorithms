import sys


def is_prime(num):
    root_num = num ** 0.5
    chk = False
    if num < 2:
        return False
    elif num == 2:
        return True
    div = 2
    while div <= root_num:
        if num % div == 0:
            return False
        div += 1
    return True


n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))

n_prime = 0

for i in range(n):
    if is_prime(x[i]):
        n_prime += 1

print(n_prime)
