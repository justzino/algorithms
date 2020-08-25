import sys

def GCD(a, b):
    if a % b == 0:
        return b
    else:
        return GCD(b, a % b) 

cnt = int(sys.stdin.readline().rstrip())
for i in range(cnt):
    result = 0
    numbers = list(map(int, sys.stdin.readline().rstrip().split()))

    for i in range(1, numbers[0]):
        for j in numbers[i+1:]:
            result += GCD(numbers[i], j)
    
    print(result)


