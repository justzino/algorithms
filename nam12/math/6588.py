# 우선 에라토스테네스의 체를 알아야 한다.

import sys
import math

N = 1000000

prime = [True for _ in range(N+1)]

for i in range(2, int(math.sqrt(N)+1)):
    if prime[i] == True:
        for i in range(2*i, N+1, i):
            prime[i] = False

# while True:
#     num = int(sys.stdin.readline().rstrip())
#     if num == 0:
#         break

#     if num % 2 != 0:
#         print("Goldbach's conjecture is wrong.")
#         continue

#     for i in range(3, N+1, 2):
#         if prime[num - i]:
#             print("{} = {} + {}".format(num, i, num-i))
#             break
# == == == == == == == == == == == == == == == == == == == == == == == == == == =
while True:
    num = int(sys.stdin.readline().rstrip())

    if num == 0:
        break
    for i in range(3, N+1, 2):  # 홀수 소수라서 3부터 시작.
        if prime[i]:
            if prime[num - i]:
                print("{} = {} + {}".format(num, i, num-i))
                break
    else:
        print("Goldbach's conjecture is wrong.")
