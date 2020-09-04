# f(n) = f(n-1) + 2*f(n-2)
n = int(input())

mem = [0, 1, 3] + [0] * (n-2)
for i in range(3, n+1):
    mem[i] = mem[i-1] + mem[i-2] * 2
print(mem[n] % 10007)
