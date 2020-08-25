import sys

A, B, C, D = sys.stdin.readline().rstrip().split()

A = A + B
C = C + D

print(int(A) + int(C))
