def dp(n):
    for i in range(3, n+1):
        mem[i] = mem[i-1] + mem[i-2]
    return mem[n]


x = int(input())
mem = [0, 1, 2] + [0] * (x - 2)

print(dp(x) % 10007)
