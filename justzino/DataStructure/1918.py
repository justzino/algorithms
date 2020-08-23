# 맞는데 왜 틀렸다 나오는지 모름...
# 괄호 갯수같은거 안맞을 때 예외처리?
from sys import stdin

line = list(stdin.readline().rstrip())
result, op_stack = [], []

for c in line:
    if 'A' <= c <= 'Z':
        result.append(c)
    elif c == '(':
        pass
    elif c == ')':
        result.append(op_stack.pop())
    else:
        op_stack.append(c)
result.append(op_stack.pop())

print(''.join(result))
