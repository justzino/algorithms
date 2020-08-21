class Stack():

    def __init__(self):
        self.stack_list = []

    def size(self):
        return len(self.stack_list)

    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def push(self, X):
        if X.isdigit():
            self.stack_list.append(X)
    
    def pop(self):
        if self.size() == 0:
            return -1
        else:
            num = self.stack_list[-1]
            del self.stack_list[-1]
            return num

    def top(self):
        if self.size() == 0:
            return -1
        else:
            return self.stack_list[-1]
    

temp_stack = Stack()

import sys

cnt = sys.stdin.readline().rstrip()

# cnt = int(input())
cnt = int(cnt)
if 1 <= cnt and cnt <= 10000:

    while_cnt = 0
    while True:

        if while_cnt == cnt:
            break
        else:
            while_cnt += 1

        # command = input()
        command = sys.stdin.readline().rstrip().split()

        if command[0] == 'size':
            print(temp_stack.size())
        elif command[0] == 'empty':
            print(temp_stack.empty())
        elif command[0] == 'top':
            print(temp_stack.top())
        elif command[0] == 'pop':
            print(temp_stack.pop())
        elif command[0] == 'push':
            temp_stack.push(command[1])

    
# https://hwiyong.tistory.com/185