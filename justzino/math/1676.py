# sol 1
# n = int(input())
# result, cnt = 1, 0
#
# for i in range(1, n+1):
#     result *= i
#
# while result % 10 == 0:
#     cnt += 1
#     result = result // 10
#
# print(cnt)
#

# sol 2
from math import factorial

cnt = 0
n = factorial(int(input()))
while n % 10 == 0:
    n = n // 10
    cnt += 1
print(cnt)
