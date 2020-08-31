import sys

string = sys.stdin.readline().rstrip()

bar = 0
sum = 0

for i in range(len(string)):

    if string[i] == '(':
        bar += 1

    elif string[i] == ')':

        bar -= 1

        if string[i-1] == '(':
            sum += bar

        elif string[i-1] == ')':
            sum += 1
print(sum)
