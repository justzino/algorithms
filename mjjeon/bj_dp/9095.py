import sys

T = int(sys.stdin.readline())

D = [0] * 12
D[1] = 1
D[2] = 2
D[3] = 4
for i in range(4, 12):
    D[i] = D[i-1] +  D[i-2] +  D[i-3]

for i in range(T):
    print(D[int(sys.stdin.readline())])


# * 1,2,3 으로 이루어짐
# * 1개 이상으로 이루어짐

# 문제를 잘 읽자..
# 1,2,3 이 아닌 i 보다 작은 수이며 2개 이상으로 이루어진 점화식..
# D = [0] * 12
# D[1] = 1
# D[2] = 1 
# for i in range(3, 12):
#     idx = 1
#     while i - idx > 1:
#         D[i] += D[i-idx] + 1
#         idx += 1