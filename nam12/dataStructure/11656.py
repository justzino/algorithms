import sys

string = sys.stdin.readline().rstrip()

ans = []

for i in range(len(string)):
    ans.append(string[i:])

ans.sort()

for i in ans:
    print(i)
