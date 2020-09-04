n = int(input())
D = [0] * 1001
D[1] = 1
D[2] = 2
for i in range(3, n+1):
    D[i] = D[i-1] + D[i-2]

print(D[n]%10007)

# 점화식 잘못세움
# 2x6 에서 좌측에 1x2 짜리 놓고 할 수 있는 방법을 찾아보고 나서 알게됨..
# n = int(input())
# D = [0] * 1001
# D[2] = 2
# for i in range(3, n+1):
#     if i%2 == 0:
#         D[i] = D[i -2] * 2
#     else:
#         D[i] = D[i-1] * 2 - 1

# print(D[n]%10007)