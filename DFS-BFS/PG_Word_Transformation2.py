# 내 풀이 - 맞음, BFS 사용
# 코드가 깔끔하지 못한 것 같음
from collections import deque


def judge_adj(word1, word2):
    length = len(word1)
    flag = 0
    for i in range(length):
        if flag > 1:
            return -1       # 문자가 2개 이상 다르면 return -1
        if word1[i] == word2[i]:
            continue
        else:
            flag += 1

    if flag == 1:           # 문자가 하나만 다르면 return 1
        return 1
    elif flag == 0:
        return 0            # 문자가 똑같으면 return 0


def solution(begin, target, words):
    if not (target in words):
        return 0
    length = len(words)
    adj = [[] for _ in range(length)]

    def bfs(v):
        counts = [1e9] * length
        counts[v] = 1
        min_count = 1e9
        q = deque([v])
        while q:
            v = q.popleft()
            if not visited[v]:
                visited[v] = True

                if words[v] == target:
                    min_count = min(counts[v], min_count)

                for edge in adj[v]:
                    if not visited[edge]:
                        counts[edge] = min(counts[v] + 1, counts[edge])
                        q.append(edge)
        return min_count

    starts = []
    for i in range(length):
        if judge_adj(begin, words[i]) == 1:
            starts.append(i)

        made_graph = [False] * length
        for j in range(i, length):
            made_graph[j] = True
            if judge_adj(words[i], words[j]) == 1:
                adj[i].append(j)
                adj[j].append(i)

    min_count = 1e9
    for start in starts:
        visited = [False] * length
        min_count = min(bfs(start), min_count)

    return min_count
