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


# primes = make_prime_set(1000000)
primes_bool = make_prime_set(1000000)
for line in sys.stdin:
    n = int(line)
    if n == 0:
        break
    for i in range(3, n // 2 + 1, 2):      # 시간 단축 2
        # if n-i in primes:
        if primes_bool[n-i] and primes_bool[i]:
            print('{} = {} + {}'. format(n, i, n-i))
            break
        if i >= n-1:
            print("Goldbach's conjecture is wrong.")
            break
