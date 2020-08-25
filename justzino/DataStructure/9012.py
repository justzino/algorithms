import sys

n = int(sys.stdin.readline())

for _ in range(n):
    line = list(sys.stdin.readline().rstrip())
    cnt = 0

    for c in line:
        if c == '(':
            cnt += 1
        elif c == ')':
            cnt -= 1
        if cnt < 0:
            print('NO')
            break
    if cnt > 0:
        print('NO')
    elif cnt == 0:
        print('YES')

    # stack = []
    # for c in line:
    #     if c == '(':
    #         stack.append(c)
    #     elif c == ')' and stack.pop() == '(':
    #         pass
    # ')))(((' 못하겠당...
    #     elif stack:
    #
    #
    #     else:
    #         print('NO')
