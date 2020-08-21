# 1st idea,자료구조 사용 x, 문자열 편집으로 푸다가 실패
# from sys import stdin
#
# string = stdin.readline().rstrip().split()
#
# for c in string:
#     len_c = len(c)
#     i = 0
#     while i <= len_c:
#         if c[i] == '<':
#             while c[i] != '>':
#                 print(c[i], end='')
#                 i += 1
#         else:
#             print(c[i::-1], end=' ')
#             i += 1

# 2nd idea
# deque를 쓰면 쉽게 풀 수 있을 것 같다는 생각이 들었다.
# 글자를 <>사이는 queue 특성을 이용하여 popleft()로,
# 역순은 stack 특성을 이용하여 pop 시키면 될것 같다.
# 파이썬에서 deque는 from collections import deque 를 이용한다.
# 결론 : deque 특성 이용 안함. 그냥 역순으로 하는 부분만 stack이용하면 됨
from sys import stdin
from collections import deque


dq = deque()
dq_ext = dq.extend      # 속도 저하 방지
line = list(stdin.readline().rstrip())
n_line = len(line)
i = 0

while i < n_line:
    if line[i] == '<':
        while dq:
            print(dq.pop(), end='')
        while line[i] != '>':
            print(line[i], end='')
            i += 1
        print(end='>')
        i += 1
    elif line[i] == ' ':
        while dq:
            print(dq.pop(), end='')
        print(end=' ')
        i += 1
    else:
        dq_ext(line[i])     # dq.extend(line[i])
        i += 1

while dq:
    print(dq.pop(), end='')



# 3rd idea
# 2nd idea로 풀다가 stack만써도 가능하겠다고 생각.
# stack 사용
# '<'열리면 '>' 까지 그대로, 나머지는 '<'나 ' '까지 stack에 넣었다가 '<'나 ' '만나면 pop
from sys import stdin


stack = []
stack_append = stack.append      # 속도 저하 방지
line = list(stdin.readline().rstrip())
n_line = len(line)
i = 0

while i < n_line:
    if line[i] == '<':
        while stack:
            print(stack.pop(), end='')
        while line[i] != '>':
            print(line[i], end='')
            i += 1
        print(end='>')
        i += 1
    elif line[i] == ' ':
        while stack:
            print(stack.pop(), end='')
        print(end=' ')
        i += 1
    else:
        stack_append(line[i])     # dq.extend(line[i])
        i += 1

while stack:
    print(stack.pop(), end='')


# solution
# s = input()
#
# tmp, ans, ck = '', '', False
#
# for i in s:
#     if i == '':
#         if not ck:
#             ans += tmp[::-1] + i
#             tmp = ''
#         else:
#             ans += i
#     elif i == '<':
#         ck = True
#         ans += tmp[::-1] + i
#         tmp = ''
#     elif i == '>':
#         ck = False
#         ans += i
#     else:
#         if ck:
#             ans += i
#         else:
#             tmp += i
#
# ans += tmp[::-1]
# print(ans)
