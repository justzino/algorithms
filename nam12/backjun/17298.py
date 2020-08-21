import sys

N = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

ans = [-1 for i in range(N)]
max = arr[len(arr)-1]

for i in range(len(arr)-1, 0, -1):

    if max < arr[i]:
        max = arr[i]

    if arr[i-1] < arr[i]:
        ans[i-1] = arr[i]

    elif arr[i-1] < ans[i]:
        ans[i-1] = ans[i]

    elif arr[i-1] < max:
        ans[i-1] = max

for i in range(N):
    print(ans[i], end=" ")

# i부터 len(arr)까지 쭉 돌리면서하면 n^2나와서 이렇게함.
# 아오 왜 안돼 ㅐㅐㅐㅐ
