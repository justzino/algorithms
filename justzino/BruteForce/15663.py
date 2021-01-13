N, M = map(int, input().split())
nums = list(map(int, input().split()))
visited = [False for _ in range(N)]
result = list()
results = list()


def dfs(cnt):
    if cnt == M:
        results.append(result.copy())
        return
    for i in range(N):
        if visited[i]:
            continue
        result.append(nums[i])
        visited[i] = True
        dfs(cnt+1)
        result.pop()
        visited[i] = False


dfs(0)
remove_dup = list(set(map(tuple, results)))
remove_dup.sort()
for a in remove_dup:
    print(*a)
