N, M = map(int, input().split())

nums = [i for i in range(1, N+1)]
visited = [False for _ in range(N)]
result = list()


def dfs(cnt):
    if cnt == M:
        print(*result)

    for i in range(N):
        if visited[i]:
            continue
        if result and nums[i] < result[-1]:
            continue

        visited[i] = True
        result.append(nums[i])
        dfs(cnt+1)

        result.pop()
        visited[i] = False

dfs(0)
