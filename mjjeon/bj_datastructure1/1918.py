pre = input()
stack = []
op = []
for item in pre:
    if item.isupper():
        print(item, end='')
    elif item == '(':
        stack.append(item)
    elif item == ')':
        while stack[-1] == '(':
            print(stack.pop())
        stack.pop(-1)
    else:
        if item == '*' || item == '/':
            pass
        elif item == '+' || item == '-':
            pass

if op:
    stack.append(op.pop())

print(''.join(stack))