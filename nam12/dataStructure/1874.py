import sys

stack = []
ans = []
current = 1

flag = True

N = int(sys.stdin.readline().rstrip())
for i in range(N):

    inputs = int(sys.stdin.readline().rstrip())
    while inputs >= current:
        stack.append(current)
        ans.append('+')
        current += 1
    if inputs == stack[-1]:
        stack.pop()
        ans.append('-')
    else:
        flag = False

if not flag:
    print("NO")

else:
    for i in ans:
        print(i)
