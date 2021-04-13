n, m = map(int, input().split())
data = [[] for _ in range(n)]
min_nums = [0 for _ in range(n)]

for i in range(n):
    data[i] = list(map(int, input().split()))
    # 현재 줄에서 가장 작은 수
    min_nums[i] = min(data[i])

# 가장 작은 수들 중 가장 큰 수 츌력
print(max(min_nums))
