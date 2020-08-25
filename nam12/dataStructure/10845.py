import sys

queue = []


def Push(x):
    queue.append(x)


def Size():
    return len(queue)


def Empty():
    if Size() == 0:
        return 1
    else:
        return 0


def Pop():
    if Empty():
        return -1
    else:
        return queue.pop(0)


def Front():
    if Empty():
        return -1
    else:
        return queue[0]


def Back():
    if Empty():
        return -1
    else:
        return queue[-1]


N = int(sys.stdin.readline().rstrip())


for i in range(N):

    cmd = sys.stdin.readline().rstrip().split()

    if cmd[0] == 'push':
        Push(cmd[1])
    elif cmd[0] == 'pop':
        print(Pop())
    elif cmd[0] == 'size':
        print(Size())
    elif cmd[0] == 'empty':
        print(Empty())
    elif cmd[0] == 'front':
        print(Front())
    elif cmd[0] == 'back':
        print(Back())
