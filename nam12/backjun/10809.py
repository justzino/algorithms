import sys

imput = sys.stdin.readline().rstrip()
N = int(input)

stack = [0 for _ in range(4)]
ans = [0, 0, 0, 0]

for i in range(N):

    string = input
    if 97 <= ord(string[i]) <= 122:
        ans[0] += 1
    elif 65 <= ord(string[i]) <= 90:
        ans[1] += 1
    elif 48 <= ord(string[i]) <= 57:
        ans[2] += 1
    else:
        ans[3] += 1
