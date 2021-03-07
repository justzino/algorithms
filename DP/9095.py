# a(n) = a(n-1) + a(n-2) + a(n-3)
T = int(input())

for _ in range(T):
    n = int(input())
    mem = [0, 1, 2, 4] + [0] * (n - 3)
    for i in range(4, n + 1):
        mem[i] = mem[i-1] + mem[i-2] + mem[i-3]
    print(mem[n])
