# 런타임 에러
import sys

n = int(sys.stdin.readline())
numbers = [0] * n
D = [0] * (n+1)
for i in range(n):
    numbers[i] = int(sys.stdin.readline())
D[0] = 0
D[1] = numbers[0]
D[2] = numbers[0] + numbers[1]

for i in range(3, n+1):
    a = D[i-1]
    b = D[i-2] + numbers[i-1]
    c = D[i-3] + numbers[i-2] + numbers[i-1]
    D[i] = max(a, b, c)

print(D[n])
