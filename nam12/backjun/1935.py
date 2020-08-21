import sys


def push(x):
    stack.append(string[x])


N = int(sys.stdin.readline().rstrip())

string = sys.stdin.readline().rstrip()

stack = []

for i in range(len(string)):
    if string[i] == 'A-Z':
