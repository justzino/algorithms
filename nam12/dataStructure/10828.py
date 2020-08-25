import sys


def push(x):
    stack.append(x)


def pop():
    try:
        print(stack.pop())
    except:
        print(-1)


def size():
    print(len(stack))


def empty():

    if len(stack) == 0:
        print(1)
    else:
        print(0)


def top():
    try:
        print(stack[-1])
    except:
        print(-1)


N = int(sys.stdin.readline().rstrip())

stack = []

for _ in range(N):

    ctrl = sys.stdin.readline().rstrip().split()

    if ctrl[0] == 'push':
        push(ctrl[1])
    elif ctrl[0] == 'pop':
        pop()
    elif ctrl[0] == 'size':
        size()
    elif ctrl[0] == 'empty':
        empty()
    elif ctrl[0] == 'top':
        top()
