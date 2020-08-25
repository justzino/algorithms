from sys import stdin


class Que:
    def __init__(self):
        self.que = []

    def push(self, x):
        self.que.append(x)

    def pop(self):
        if self.que:
            front = self.que[0]
            del self.que[0]
            return front
        else:
            return -1

    def size(self):
        return len(self.que)

    def empty(self):
        if len(self.que) == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.que:
            return self.que[0]
        else:
            return -1

    def back(self):
        if self.que:
            return self.que[-1]
        else:
            return -1


n = int(stdin.readline())

que = Que()     # 괄호 붙여야 함

# for line in stdin:
for i in range(n):
    line = stdin.readline().rstrip().split()
    if line[0] == 'push':
        que.push(int(line[1]))
    elif line[0] == 'pop':
        print(que.pop())
    elif line[0] == 'size':
        print(que.size())
    elif line[0] == 'empty':
        print(que.empty())
    elif line[0] == 'front':
        print(que.front())
    elif line[0] == 'back':
        print(que.back())
