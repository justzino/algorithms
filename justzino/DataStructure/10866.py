from sys import stdin


class Deque:
    def __init__(self):
        self.deque = []

    def push_front(self, x):
        self.deque.insert(0, x)

    def push_back(self, x):
        self.deque.append(x)

    def pop_front(self):
        if self.deque:
            x = self.deque[0]
            del self.deque[0]
            return x
        else:
            return -1

    def pop_back(self):
        if self.deque:
            return self.deque.pop()
        else:
            return -1

    def size(self):
        return len(self.deque)

    def empty(self):
        # 덱이 있는 경우
        if self.deque:
            return 0
        # 덱이 비어 있는 경우
        else:
            return 1

    def front(self):
        if self.deque:
            return self.deque[0]
        else:
            return -1

    def back(self):
        if self.deque:
            return self.deque[-1]
        else:
            return -1


n = int(stdin.readline())

deque = Deque()

for i in range(n):
    op = stdin.readline().rstrip().split()

    if op[0] == 'push_front':
        deque.push_front(op[1])
    elif op[0] == 'push_back':
        deque.push_back(op[1])
    elif op[0] == 'pop_front':
        print(deque.pop_front())
    elif op[0] == 'pop_back':
        print(deque.pop_back())
    elif op[0] == 'size':
        print(deque.size())
    elif op[0] == 'empty':
        print(deque.empty())
    elif op[0] == 'front':
        print(deque.front())
    elif op[0] == 'back':
        print(deque.back())