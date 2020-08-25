import sys

def GCM(a, b): 
    if a%b == 0:
        return b
    else:
        return GCM(b, a%b)

def LMC(a, b):
    return int(a*b/GCM(a, b))

cnt = int(sys.stdin.readline().rstrip())

for i in range(cnt):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(LMC(a, b))
