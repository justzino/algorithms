N, K = map(int, input().split())

weights = []
values = []

for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

dp = [0] * (K+1)

for w, v in zip(weights, values):
    for i in range(K, w-1, -1):
        dp[i] = max(dp[i], dp[i-w] + v)

result = dp[K]
print(result)
