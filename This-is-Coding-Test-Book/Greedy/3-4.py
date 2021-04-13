n, k = map(int, input().split())
result = 0

while True:
    # N 이 k 로 나누어 떨어지는 수가 될 때까지 1씩 빼는 것 한번에 계산
    target = (n // k) * k
    result += (n - target)
    n = target

    # n이 k보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        # 마지막 남은 수에 대해 1을 뺀 후 더함
        result += (n - 1)
        break

    result += 1
    n //= k

print(result)
