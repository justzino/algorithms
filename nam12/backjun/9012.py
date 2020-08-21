import sys

N = int(sys.stdin.readline().rstrip())

for _ in range(N):

    string = (sys.stdin.readline().rstrip())
    stack = 0

    for char in string:
        print(char)
        if char == '(':
            stack += 1
        elif char == ')':
            stack -= 1

    if stack == 0:
        print("YES")
    else:
        print("NO")
