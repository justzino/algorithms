
# def minus_binary(n):

#     sum = 0
#     i = 0
#     for i in range(20):
#         sum += (-2)**i
#         print(sum)
#         if sum == n:
#             break
#         i += 1


# print(minus_binary(-13))

# 원래 짰던 코드 0을 고려안해주고 짰음.

import sys

N = int(sys.stdin.readline().rstrip())

ans = ''

while N:
    if N % (-2) == 0:  # 나눠질 때.
        ans = '0' + ans  # ans가 뒤에 와야함
        N = N//(-2)
    else:
        ans = '1' + ans
        N = N//(-2) + 1
print(ans)
