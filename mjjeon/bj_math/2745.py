import sys
N, B = map(str, sys.stdin.readline().rstrip().split())

result = 0
b = 0
B = int(B)
for i in str(N)[::-1]:
    if i.isupper():
        result += (ord(i) - 55) * (B**b)
    else:
        result += int(i)*(B**b)
    b += 1
print(result)
