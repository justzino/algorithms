import sys

string = sys.stdin.readline().rstrip()
ans = []

for i in range(len(string)):

    if string[i].isupper():
        if ord(string[i]) + 13 > ord('Z'):
            ans[i] = ord(string[i])-13
        else:
            ans[i] = ord(string[i])+13

    elif string[i].islower():
        if ord(string[i]) + 13 > ord('z'):
            ans[i] = ord(string[i])-13
        else:
            ans[i] = ord(string[i])+13
    else:
        ans[i] = ord(string[i])

    print(ans[i], end="")
