from itertools import permutations


def make_prime_table(n):
    primes = [True for _ in range(n + 1)]
    max_q = int(n ** (1 / 2))
    primes[0] = False
    primes[1] = False

    for i in range(2, max_q + 1):
        if i == False:
            continue

        j = 2
        while i * j <= n:
            primes[i * j] = False
            j += 1

    return primes


def solution(numbers):
    nums = []
    primes = []

    for i in range(1, len(numbers) + 1):
        nums += list(map(list, set(permutations(numbers, i))))

    for i in range(len(nums)):
        primes.append(int("".join(nums[i])))

    primes = list(set(primes))
    max_ = max(primes)

    if max_ < 2:
        return 0

    answer = 0
    prime_table = make_prime_table(max_)

    for prime in primes:
        if prime_table[prime]:
            answer += 1

    return answer