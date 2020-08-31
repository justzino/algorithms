def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    root_num = num ** 0.5
    div = 2
    while div <= root_num:
        if num % div == 0:
            return False
        div += 1
    return True


m, n = map(int, input().split())
prime = []

while m <= n:
    if is_prime(m):
        prime.append(m)
    m += 1

print(*prime)

# 위처럼 짜는 건 쉽지만, prime 구한 부분 반복하는 거 너무 비효율적인데.. 이거 prime 먼저하고 그다음 큰수 하는게 맞을듯
# but... 몇번을 짜보았으나 실패.. 이유 찾자
# def is_prime(num):
#     if num < 2:
#         return False
#     elif num == 2:
#         return True
#     root_num = num ** 0.5
#
#     if num <= prime_list[-1]:
#         for i in prime_list:
#             if num == i:
#                 return True
#             elif num < i:
#                 return False
#     elif root_num <= prime_list[-1] < num:
#         for i in prime_list:
#             if num % i == 0:
#                 return False
#             elif i > root_num:
#                 return True
#     else:       # prime_list[-1] < root_num
#         for i in prime_list:
#             if num % i == 0:
#                 return False
#         div = prime_list[-1] + 1
#         while div <= root_num:
#             if num % div == 0:
#                 return False
#             div += 1
#         prime_list.append(div-1)
#         return True
#
#
# m, n = map(int, input().split())
# result = []
# prime_list = [2, 3]
#
# while m <= n:
#     if is_prime(m):
#         result.append(m)
#     m += 1
#
# print(*result)
