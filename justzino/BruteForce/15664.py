N, M = map(int, input().split())
nums = list(map(int, input().split()))
visited = [False for _ in range(N)]
results = list()
result = list()


def dfs(cnt):
    if cnt == M:
        results.append(tuple(result))
        return

    for i in range(N):
        if visited[i]:
            continue
        if result and result[-1] > nums[i]:
            continue
        result.append(nums[i])
        visited[i] = True
        dfs(cnt+1)
        result.pop()
        visited[i] = False


dfs(0)
remove_dup_results = list(set(results))
remove_dup_results.sort()
for result in remove_dup_results:
    print(*result)
