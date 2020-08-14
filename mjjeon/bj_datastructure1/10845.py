import sys

class Queue():
    def __init__(self):
        self.queue = []

    def size(self):
        return len(self.queue)

    def empty(self):
        if len(self.queue) == 0:
            return 1
        else:
            return 0

    def push(self, X):
        self.queue.append(X)

    def pop(self):
        if self.empty() == 0:
            pop_print = self.queue[0]
            del self.queue[0]
            return pop_print
        else:
            return -1

    def front(self):
        if self.empty() == 0:
            return self.queue[0]
        else:
            return -1  

    def back(self):
        if self.empty() == 0:
            return self.queue[-1]
        else:
            return -1  

temp_queue = Queue()

cmd_cnt = int(sys.stdin.readline().rstrip())

if 1 <= cmd_cnt <= 10000:

    for i in range(cmd_cnt):

        cmd = sys.stdin.readline().rstrip().split()

        if cmd[0] == 'push':
            temp_queue.push(cmd[1])
        elif cmd[0] == 'pop':
            print(temp_queue.pop())
        elif cmd[0] == 'size':
            print(temp_queue.size())
        elif cmd[0] == 'empty':
            print(temp_queue.empty())
        elif cmd[0] == 'front':
            print(temp_queue.front())
        elif cmd[0] == 'back':
            print(temp_queue.back())
