import sys

while True:

    try:
        ans = [0, 0, 0, 0]
        string = sys.stdin.readline().rstrip()
        for i in range(len(string)):
            if string[i].islower():
                ans[0] += 1
            elif string[i].isupper():
                ans[1] += 1
            elif string[i].isdigit():
                ans[2] += 1
            else:
                ans[3] += 1

        for i in range(4):
            print(ans[i], end=" ")
        print("")

    except:
        break
