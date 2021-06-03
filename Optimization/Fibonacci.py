# 기본 재귀 풀이1 - O(2^n)
def fibo1(n):
    return fibo1(n-1) + fibo1(n-2) if n >= 2 else n


# 반복문 사용 O(n)
def fibo2(n):
    if n < 2:
        return n

    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a + b

    return b


# DP - 반복문 (bottom-up) - O(n)
def fibo3(n):
    if n < 2:
        return n
    dp = [0 for _ in range(n+1)]
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


# DP - 재귀 (top-down) - O(n)
def fibo4(n):
    dp = [-1 for _ in range(n+1)]

    def iterate(n):
        if n < 2:
            return n

        if dp[n] != -1:
            return dp[n]

        dp[n] = iterate(n-1) + iterate(n-2)
        return dp[n]

    return iterate(n)


print(fibo2(35))
print(fibo3(35))
print(fibo4(35))
print(fibo1(35))
