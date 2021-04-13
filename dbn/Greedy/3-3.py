n, m = map(int, input().split())
data = [[] for _ in range(n)]
min_nums = [0 for _ in range(n)]

for i in range(n):
    data[i] = list(map(int, input().split()))
    min_nums[i] = min(data[i])

print(max(min_nums))
