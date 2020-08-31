# 2와 5의 개수를 찾는다.
def getCount(multi, max): 
    num_cnt = 0
    div = multi
    while max >= div:
        num_cnt += max // div
        div *= multi       
    return num_cnt

a, b = map(int, input().split())

# a - (b + c)
five_cnt = getCount(5, a) - getCount(5, a - b) - getCount(5, b)
two_cnt = getCount(2, a) - getCount(2, a - b) - getCount(2, b)

five_cnt = max(five_cnt, 0)
two_cnt = max(two_cnt, 0)
print(min(five_cnt, two_cnt))


# 시간초과
# def nCm(n, m):
#     n_result = 1
#     if n > 2:
#         for i in range(2, n+1):
#             n_result *= i
#     m_result = 1
#     if m > 2:
#         for i in range(2, m+1):
#             m_result *= i
#     n_m_result = 1
#     if n-m > 2:
#         for i in range(2, n-m + 1):
#             n_m_result *= i
#     return int(n_result/(n_m_result*m_result))

# def nCm(n, m):
#     if n == m or m == 0:
#         return 1
#     else:
#         return nCm(n - 1, m - 1) + nCm(n - 1, m)

# a, b = map(int, input().split())
# result = str(nCm(a, b))
# cnt = 0
# for i in result[::-1]:
#     if i == '0':
#         cnt += 1
#     else:
#         break
# print(cnt)