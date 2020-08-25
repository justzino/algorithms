import sys

string = sys.stdin.readline().rstrip()
op = []
ans = []
cnt = 10

for i in range(len(string)):

    if string[i] == '+' or string[i] == '-' or string[i] == '*' or string[i] == '/':
        op.append(string[i])  # op 담기.

    elif string[i] == '(':
        cnt += 1

    elif string[i] == ')':
        cnt -= 1

        if cnt == 10:
            while op:
                ans.append(op.pop())
    else:
        ans.append(string[i])

for i in range(len(ans)):
    print(ans[i], end="")
