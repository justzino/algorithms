# 틀림 - DFS 로 구현
# 같은 단계에서 만들어지는 경우를 먼저 다 확인하면서 넘어가야 최소 값을 구할 수 있는데, DFS로 구현해서 최소 count를 구현하려다 보니 실패

def judge(word1, word2):
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

    def dfs(v, count):
        if words[v] == target:
            counts.append(count)
            print(counts)
            return count
        if not visited[v]:
            visited[v] = True
            for edge in adj[v]:
                count += 1
                dfs(edge, count)

    starts = []
    for i in range(length):
        if judge(begin, words[i]) == 1:
            starts.append(i)

        made_graph = [False] * length
        for j in range(length):
            made_graph[j] = True
            if judge(words[i], words[j]) == 1:
                adj[i].append(j)
                adj[j].append(i)

    min_count = 1e9
    for start in starts:
        visited = [False] * length
        counts = []
        dfs(start, 0)
        min_count = min(min(counts), min_count)
        print(min_count)

    return min_count


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))
