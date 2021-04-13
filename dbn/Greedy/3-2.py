n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True)
used = [0 for _ in range(n)]

result = 0

for _ in range(m):
    if used[0] < 3:
        result += nums[0]
        used[0] += 1
    else:
        result += nums[1]
        used[0] = 0

print(result)
