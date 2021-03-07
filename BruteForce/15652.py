N, M = map(int, input().split())
nums = [i for i in range(1, N+1)]
result = list()


def dfs(cnt):
    if cnt == M:
        print(*result)
        return

    for i in range(N):
        if result and result[-1] > nums[i]:
            continue
        result.append(nums[i])
        dfs(cnt+1)
        result.pop()


dfs(0)
