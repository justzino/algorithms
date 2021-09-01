N = int(input())
# ord('a') = 97
# ord('z') = 122

def get_length(arr, k):
    left, right = 0, k-1
    min_ = 10001
    max_ = 0
    while right < len(arr):
        min_ = min(arr[right] - arr[left] + 1, min_)
        max_ = max(arr[right] - arr[left] + 1, max_)
        left += 1
        right += 1
    return min_, max_


for _ in range(N):
    string = input().rstrip()
    K = int(input())
    idx_alpha = [[] for _ in range(26)]
    n_alpha = [0 for _ in range(26)]

    for i in range(len(string)):
        idx_alpha[ord(string[i]) - 97].append(i)
        n_alpha[ord(string[i]) - 97] += 1

    # k 가 없으면 -1
    if max(n_alpha) < K:
        print(-1)
        continue

    min_result = []
    max_result = []
    # 정확히 K개를 포함하는 가장 짧은 연속 문자열 길이
    for i in range(26):
        if n_alpha[i] < K:
            continue
        x, y = get_length(idx_alpha[i], K)
        min_result.append(x)
        max_result.append(y)

    print(min(min_result), max(max_result))