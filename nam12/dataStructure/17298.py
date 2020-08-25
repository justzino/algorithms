import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

ans = [-1 for i in range(N)]
stack = []

for i in range(len(arr)):

    while stack and arr[stack[-1]] < arr[i]:
        ans[stack.pop()] = arr[i]

    stack.append(i)

for i in ans:
    print(i, end=" ")
