import sys

N, B = map(int, sys.stdin.readline().rstrip().split())

ans = []

while N:
    if N % B != 0:
        ans.append(N % B)
        N //= B
    else:
        ans.append(0)
        N //= B

for i in ans[::-1]:
    if i > 9:
        i = chr(i+55)
    print(i, end="")
