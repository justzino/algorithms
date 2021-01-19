from itertools import combinations_with_replacement
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()


def dfs(cnt):
    seqs = combinations_with_replacement(nums, cnt)
    results = list(set(seqs))
    results.sort()

    for seq in results:
        print(*seq)


dfs(M)
