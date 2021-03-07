# sol 1
# n = int(input())
#
# for i in range(n):
#     a, b = map(int, input().split())
#     print("Case #{}: {} + {} = {}".format(i + 1, a, b, a + b))

# sol 2
import sys

n = int(input())

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #{}: {} + {} = {}".format(i + 1, a, b, a + b))
