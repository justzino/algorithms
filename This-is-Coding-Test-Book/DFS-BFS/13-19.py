n = int(input())
seq = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())   # [+, -, *, //]

max_value = -1e9
min_value = 1e9


def dfs(i, now):
    global max_value, min_value, add, sub, mul, div

    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)

    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + seq[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - seq[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * seq[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now // seq[i]))
            div += 1


dfs(1, seq[0])

print(max_value)
print(min_value)


"""
수열: N개의 수 -> 순서 그대로
연산자: N-1개, [+, -, *, //]

연산결과 최대, 최고값 구하기
"""