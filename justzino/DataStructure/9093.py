import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    string = list(sys.stdin.readline().rstrip().split(' '))

    for c in string:
        print(c[::-1], end=' ')
    print()     # 개행
