pre = input()
stack = []
op = []
priority = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
for item in pre:
    if item.isupper():
        print(item, end='')
    elif item == '(':
        stack.append(item)
    elif item == ')':
        while stack and stack[-1] != '(':
            print(stack.pop(), end='')
        stack.pop()
    else:
        while stack and priority[item] <= priority[stack[-1]]:
            print(stack.pop(), end='')
        stack.append(item)

if stack:
    print(''.join(stack[::-1]))
