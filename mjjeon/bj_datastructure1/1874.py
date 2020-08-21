import sys

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

cnt = int(sys.stdin.readline().rstrip())
result_list = []
while_cnt = 0
count = 1

while while_cnt < cnt:
    command = int(sys.stdin.readline().rstrip())
    while count <= command:
        temp_stack.push(count)
        result_list.append('+')
        count += 1
    if temp_stack.top() == command:
        temp_stack.pop()
        result_list.append('-')
    else:
        print("NO")
        break

    while_cnt += 1

if while_cnt == cnt:
    print('\n'.join(result_list))

# if 1 <= cnt and cnt <= 100000:

#     while_cnt = 0
#     temp_list = [i for i in range(1, cnt+1)]
#     result_list = []
#     while while_cnt < cnt:
#         command = int(sys.stdin.readline().rstrip())
#         if temp_stack.top() == command:
#             temp_stack.pop()
#             result_list.append('-')
#         else:
#             if command in temp_list:
#                 while command in temp_list and len(temp_list) != 0:
#                     temp_stack.push(temp_list[0])
#                     result_list.append('+')
#                     del temp_list[0]
#                 temp_stack.pop()
#                 result_list.append('-')
#             else:
#                 if command <= temp_stack.top():
#                     while command <= temp_stack.top() and temp_stack.size() != 0:
#                         temp_stack.pop()
#                         result_list.append('-')
#                 else:
#                     print("NO")
#                     break
#         while_cnt += 1
#     if while_cnt == cnt:
#         print('\n'.join(result_list))