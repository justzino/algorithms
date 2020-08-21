import sys

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    text = sys.stdin.readline().rstrip().split()

    for char in text:
        print(char[::-1], end=" ")
    print("")
