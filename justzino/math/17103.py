import sys


# 에라토스의 체
def make_prime_set(num):
    sieve = [False, False] + [True] * (num - 1)
    root = int(num ** 0.5)              # 시간 단축1

    for i in range(2, root + 1):        # 시간 단축1
        if sieve[i]:
            for j in range(2*i, num+1, i):      # i의 배수 지우기
                sieve[j] = False

    # return [i for i in range(2, num+1) if sieve[i]]
    return sieve


primes_bool = make_prime_set(1000000)
T = int(sys.stdin.readline())
for line in sys.stdin:
    N = int(line)
    numCase = 0

    if N == 4:      # 유일한 예외 경우 : 4 = 2 + 2
        numCase = 1
    else:
        for i in range(3, N // 2 + 1, 2):      # 시간 단축 2
            # if n-i in primes:
            if primes_bool[N-i] and primes_bool[i]:
                numCase += 1
    print(numCase)
