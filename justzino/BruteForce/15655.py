N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visited = [False for _ in range(N)]
result = list()


def dfs(cnt):
    if cnt == M:
        print(*result)
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
