N, M = map(int, input().split())
nums = list(map(int, input().split()))
seq = list()
seqs = list()


def dfs(cnt):
    if cnt == M:
        seqs.append(seq.copy())
        return

    for i in range(N):
        seq.append(nums[i])
        dfs(cnt+1)
        seq.pop()


dfs(0)
results = list(set(map(tuple, seqs)))
results.sort()
for result in results:
    print(*result)
