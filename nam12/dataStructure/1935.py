# 코드가 날라감....
# while 3개 써서 i<N 까지
# string[i]가 isupper 면 입력받은 값 넣어주고
# operator였으면 pop 2번한거 계산하고 다시 push했었음.

import sys

N = int(sys.stdin.readline().rstrip())
string = sys.stdin.readline().rstrip()

stack = []
input = []
ans = []

for i in range(N):
    input.append(int(sys.stdin.readline().rstrip()))
input.reverse()

for i in range(len(string)):

    if string[i].isupper():
        stack.append((input.pop()))

    else:
        first = stack.pop()
        second = stack.pop()

        if string[i] == '*':

        elif string[i] == '/':

        elif string[i] == '+':

        elif string[i] == '-':
