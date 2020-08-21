import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

queue = []
for i in range(N):
    queue.append(i+1)
# queue = [i for i in range(1, N+1)]로 표현 가능

ans = []
index = 0

for i in range(N):
    index += K-1  # 한칸식 줄어드므로 K-1

    if index >= len(queue):
        index = index % len(queue)
    ans.append(queue.pop(index))

print("<", end="")
for i in range(N-1):
    print(ans[i], end=", ")
print(ans[N-1], end=">")
