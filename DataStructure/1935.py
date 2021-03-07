from sys import stdin

num = {}

N = int(stdin.readline())
exp = list(stdin.readline().rstrip())
stack = []

for i in range(N):
    num[chr(65+i)] = int(stdin.readline())      # {'A' : 1}

for c in exp:
    if 64 < ord(c) < 91:
        stack.append(num[c])
    elif c == '+':
        stack.append(stack.pop() + stack.pop())
    elif c == '*':
        stack.append(stack.pop() * stack.pop())
    elif c == '-':
        stack.append(-stack.pop() + stack.pop())
    elif c == '/':
        divisor = stack.pop()
        stack.append(stack.pop() / divisor)
print('{0:.2f}'.format(stack.pop()))