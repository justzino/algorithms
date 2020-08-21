import sys


def push_front(x):
    d.insert(0, x)


def push_back(x):
    d.append(x)


def pop_front():
    if d:
        return d.pop(0)
    else:
        return -1


def pop_back():
    if d:
        return d.pop(-1)
    else:
        return -1


def size():
    return len(d)


def empty():
    if not d:
        return 1
    else:
        return 0


def front():

    if d:
        return d[0]
    else:
        return -1


def back():

    if d:
        return d[-1]
    else:
        return -1


N = int(sys.stdin.readline().rstrip())
d = []

for i in range(N):

    cmd = sys.stdin.readline().rstrip().split()

    if cmd[0] == "push_front":
        push_front(cmd[1])
    elif cmd[0] == "push_back":
        push_back(cmd[1])
    elif cmd[0] == "pop_front":
        print(pop_front())
    elif cmd[0] == "pop_back":
        print(pop_back())
    elif cmd[0] == "size":
        print(size())
    elif cmd[0] == "empty":
        print(empty())
    elif cmd[0] == "front":
        print(front())
    elif cmd[0] == "back":
        print(back())
