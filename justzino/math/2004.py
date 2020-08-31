# n!
# def fac(n):
#     if n == 0 or N == 1:
#         return 1
#     else:
#         r = 1
#         for i in range(1, n+1):
#             r *= i
#     return r
#
#
# # n*(n-1)*...*(n-m+1)
# def fac2(n, m):     # nPm
#     r = 1
#     for i in range(n-m+1, n+1):
#         r *= i
#     return r
#
#
# # nCm
# def combination(n, m):
#     if m == 0:              # nC0 == 1
#         return 1
#     elif n < 2 * m:         # n-m < m 인 경우
#         return fac2(n, n-m) // fac(n-m)
#     return fac2(n, m) // fac(m)
#
#
# N, M = map(int, input().split())
# cnt = 0
# result = combination(N, M)
# print(result)
#
# while result % 10 == 0:
#     cnt += 1
#     result = result // 10
# print(cnt)


# input 으로 큰 수가 들어오므로 단순 계산 x
# 생각을 바꿔서 10 = 2*5의 개수만 세면 됨
# n! 에 곱해지는 num 의 개수 : 1,2,...,n 에서 num의 배수는 num개마다 나오는 것을 이용
def countNum(n, num):
    count = 0
    divisor = num
    while n >= divisor:
        count = count + (n // divisor)
        divisor = divisor * num
    return count


N, M = map(int, input().split())

print(min(countNum(N, 2) - countNum(M, 2) - countNum(N-M, 2), countNum(N, 5) - countNum(M, 5) - countNum(N-M, 5)))
