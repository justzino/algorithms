import sys


def push(x):
    stack.append(x)


def pop():
    try:
        return stack.pop()
    except:
        return -1


def size():
    return len(stack)


def empty():
    if stack:
        return 0
    else:
        return 1


def top():
    if stack:
        return stack[-1]
    else:
        return -1


n = int(sys.stdin.readline())
stack = []

for i in range(n):
    op = sys.stdin.readline().rstrip().split()

    if op[0] == 'push':
        push(op[1])
    elif op[0] == 'pop':
        print(pop())
    elif op[0] == 'size':
        print(size())
    elif op[0] == 'empty':
        print(empty())
    elif op[0] == 'top':
        print(top())
