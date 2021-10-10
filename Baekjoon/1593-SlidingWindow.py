N, M = map(int, input().split())
target = input().strip()
string = input().strip()

target_count = [0] * 52
string_count = [0] * 52
answer = 0

for c in target:
    if 'a' <= c <= 'z':
        target_count[ord(c) - ord('a')] += 1
    else:
        target_count[ord(c) - ord('A') + 26] += 1

# 첫 윈도우 검사
for i in range(N):
    c = string[i]
    if 'a' <= c <= 'z':
        string_count[ord(c) - ord('a')] += 1
    else:
        string_count[ord(c) - ord('A') + 26] += 1

if string_count == target_count:
    answer += 1

s = 0
for e in range(N, M):
    start = string[s]
    end = string[e]

    if 'a' <= start <= 'z':
        string_count[ord(start) - ord('a')] -= 1
    else:
        string_count[ord(start) - ord('A') + 26] -= 1

    if 'a' <= end <= 'z':
        string_count[ord(end) - ord('a')] += 1
    else:
        string_count[ord(end) - ord('A') + 26] += 1

    if string_count == target_count:
        answer += 1

    s += 1

print(answer)