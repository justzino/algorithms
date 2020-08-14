import sys
cnt = int(sys.stdin.readline().rstrip())
idx = 0
post_order = list(map(str, sys.stdin.readline().rstrip()))
stack = []
numbers = []
op = ['*', '-', '+', '/']
result = []
for i in range(cnt):
    numbers.append(int(sys.stdin.readline().rstrip()))

for item in post_order:
    if item in op:
        left = result.pop() if len(stack) == 0 else stack.pop()
        right = result.pop() if len(stack) == 0 else stack.pop()
        if item == '*':
            result.append(left*right)
        elif item == '-':
            result.append(left-right)
        elif item == '+':
            result.append(left+right)
        else:
            result.append(left/right)
    else:
        stack.append(numbers[idx])
        idx += 1
    
print(*result)
