# 런타임 에러
# import sys
#
#
# def left(cursor):
#     if cursor <= 0:
#         pass
#     else:
#         cursor -= 1
#
#
# def right(cursor):
#     if cursor >= n:
#         pass
#     else:
#         cursor += 1
#
#
# def backspace(cursor, n):
#     if cursor <= 0:
#         pass
#     else:
#         del string[cursor-1]
#         n -= 1
#         cursor -= 1
#
#
# def put(cursor, n, input):
#     string.insert(cursor, input)
#     cursor += 1
#     n += 1
#
#
# string = list(sys.stdin.readline().rstrip()) + list(' ')
# n = len(string) - 1
# cursor = n - 1
#
# for _ in range(int(sys.stdin.readline())):
#     op = list(sys.stdin.readline().rstrip())
#
#     if op[0] == 'L':
#         left(cursor)
#     elif op[0] == 'D':
#         right(cursor)
#     elif op(0) == 'B':
#         backspace(cursor, n)
#     elif op[0] == 'P':
#         put(cursor, n, op[1])
#
# for c in string:
#     print(c, end='')

import sys
# 정답
# 이 문자열은 길이가 N이고, 영어 소문자로만 이루어져 있으며, 길이는 100,000을 넘지 않는다.
# 둘째 줄에는 입력할 명령어의 개수를 나타내는 정수 M(1 ≤ M ≤ 500,000)이 주어진다.
# 시간을 줄여야함
# stack 2개를 쓰는 것이 핵심 아이디어

left_stack = list(sys.stdin.readline().rstrip())
right_stack = []

# 받아서 안씀....
_ = int(sys.stdin.readline())

for line in sys.stdin:
    if line[0] == 'L':
        if left_stack:
            right_stack.append(left_stack.pop())
        else:
            continue
    elif line[0] == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())
        else:
            continue
    elif line[0] == 'B':
        if left_stack:
            left_stack.pop()
        else:
            continue
    elif line[0] == 'P':
        left_stack.append(line[2])

print(''.join(left_stack + list(reversed(right_stack))))
# 안됨.. 왜?
# print(''.join(left_stack + right_stack.reverse()))
