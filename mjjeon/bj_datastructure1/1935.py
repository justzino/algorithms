import sys
cnt = int(sys.stdin.readline().rstrip())
post_order = list(map(str, sys.stdin.readline().rstrip()))
numbers = []
op = ['*', '-', '+', '/']
result = []

for i in range(cnt):
    numbers.append(int(sys.stdin.readline().rstrip()))

for item in post_order:
    if item in op:
        right = result.pop()
        left = result.pop()
        if item == '*':
            result.append(left*right)
        elif item == '-':
            result.append(left-right)
        elif item == '+':
            result.append(left+right)
        else:
            result.append(left/right)
    else:
        result.append(numbers[ord(item) - 65])
    
print("{0:.2f}".format(result[0]))
