import sys

class Deque():
    def __init__(self):
        self.deque = []

    def push_front(self, X):
        self.deque.insert(0, X)

    def push_back(self, X):
        self.deque.insert(self.size(), X)
        
    def pop_front(self):
        if self.empty() == 0:
            result = self.deque[0]
            del self.deque[0]
            return result
        else:
            return -1
        
    def pop_back(self):
        if self.empty() == 0:
            result = self.deque[-1]
            del self.deque[-1]
            return result
        else:
            return -1

    def size(self):
        return len(self.deque)

    def empty(self):
        if len(self.deque) == 0: 
            return 1 
        else: 
            return 0
    
    def front(self):
        if self.empty() == 0:
            return self.deque[0]
        else:
            return -1   

    def back(self):
        if self.empty() == 0:
            return self.deque[-1]
        else:
            return -1
        
deque = Deque()
cnt = int(sys.stdin.readline().rstrip())

if 1 <= cnt <= 10000:

    while cnt > 0:
        cmd = sys.stdin.readline().rstrip().split()

        if cmd[0] == 'push_front':
            deque.push_front(cmd[1])
        elif cmd[0] == 'push_back':
            deque.push_back(cmd[1])
        elif cmd[0] == 'pop_front':
            print(deque.pop_front())
        elif cmd[0] == 'pop_back':
            print(deque.pop_back())
        elif cmd[0] == 'size':
            print(deque.size())
        elif cmd[0] == 'empty':
            print(deque.empty())
        elif cmd[0] == 'front':
            print(deque.front())
        elif cmd[0] == 'back':
            print(deque.back())

        cnt -= 1