import sys
import math

M, N = map(int, (sys.stdin.readline().rstrip().split()))

for i in range(M, N+1):

    check = True

    if i < 2:
        check = False

    n = int(math.sqrt(i))
    for j in range(2, n+1):
        if i % j == 0:
            check = False
            break
    if check:
        print(i)

# 1 2를 입력했을 때 1이 나와버린다. <- 이거를 처리해줘야됨...


# def prime(n):
#     if n == 1:
#         return False
#     else:
#         for i in range(2, int(math.sqrt(n)+1)):
#             if n % i == 0:
#                 return False
#             return True


# M, N = map(int, (sys.stdin.readline().rstrip().split()))

# for i in range(M, N+1):
#     if prime(i):
#         print(i)
