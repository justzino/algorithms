n, k = map(int, input().split())

result = 0
while True:
    if n <= 1:
        break

    q, r = divmod(n, k)
    if r == 0:
        result += 1
        n = q
    else:
        result += 1
        n = n - 1

print(result)