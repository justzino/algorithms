# # 맞는데 왜 틀렸다 나오는지 모름...
# # 괄호 갯수같은거 안맞을 때 예외처리?
# from sys import stdin
#
# line = list(stdin.readline().rstrip())
# result, op_stack = [], []
#
# for c in line:
#     if 'A' <= c <= 'Z':
#         result.append(c)
#     elif c == '(':
#         pass
#     elif c == ')':
#         result.append(op_stack.pop())
#     else:
#         op_stack.append(c)
# result.append(op_stack.pop())
#
# print(''.join(result))


# sol(찾아봄)
import sys
# def priority(x):
#     if x == "*" or x == "/":
#         return 2
#     elif x == "+" or x == "-":
#         return 1
#     elif x == "(" or x == ")":
#         return 0
#
#     return -1
priority = {
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    '(': 0
}


def solve():
    stack = []
    for c in '('+sys.stdin.readline().rstrip()+')':
        if 'A' <= c <= 'Z':
            print(c, end='')
        elif c == '(':
            stack.append(c)
        elif c ==')':
            while True:
                o = stack.pop()
                if o == '(':
                    break
                print(o, end='')
        else:
            while stack[-1] != '(' and priority[c] <= priority[stack[-1]]:
                print(stack.pop(), end='')
            stack.append(c)


solve()
