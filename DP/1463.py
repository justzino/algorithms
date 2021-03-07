# bottom - up 방식 dp 사용
def dp(n):
    mem = [0, 0, 1, 1] + [0] * (n - 3)  # x == 1, 2, 3

    for i in range(4, n + 1):
        mem[i] = mem[i - 1] + 1

        if i % 3 == 0:
            mem[i] = min(mem[i // 3] + 1, mem[i])       # 이 경우도 최소로 비교해서 뽑아줘야 함
        if i % 2 == 0:
            mem[i] = min(mem[i // 2] + 1, mem[i])

    return mem[n]


x = int(input())

print(dp(x))
