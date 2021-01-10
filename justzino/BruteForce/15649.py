N, M = map(int, input().split())

num_list = [i for i in range(1, N+1)]
visited_list = [False for _ in range(N)]
result = []


def dfs(cnt):
    if cnt == M:
        print(*result)
        return

    for i in range(N):
        if visited_list[i]:
            continue
        visited_list[i] = True
        result.append(num_list[i])
        dfs(cnt + 1)

        result.pop()
        visited_list[i] = False

dfs(0)
