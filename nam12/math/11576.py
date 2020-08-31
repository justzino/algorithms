import sys

A, B = map(int, sys.stdin.readline().rstrip().split())

m = int(sys.stdin.readline().rstrip())

arr = [i for i in sys.stdin.readline().rstrip().split()]


sum, cnt = 0, 0
for i in arr[::-1]:

    sum += int(i)*(A**cnt)
    cnt += 1

ans = []
while sum:
    if sum % B != 0:
        ans.append(sum % B)
        sum //= B
    else:
        ans.append(0)
        sum //= B

for i in ans[::-1]:
    print(i, end=" ")
