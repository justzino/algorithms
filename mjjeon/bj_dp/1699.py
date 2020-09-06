N = int(input())

D = [0] * (N+1)
for i in range(1, N+1):
    D[i] = i
    
    for j in range(1, i):
        if (j*j) > i:
            break
        if D[i] > D[i - j*j] + 1:
            D[i] = D[i - j*j] + 1
    
print(D[N])

# min -> if: https://hjp845.tistory.com/123
# 또 시간초과: https://somjang.tistory.com/entry/BaeKJoon-1699%EB%B2%88-%EC%A0%9C%EA%B3%B1%EC%88%98%EC%9D%98-%ED%95%A9-Python
# N = int(input())

# D = [0] * (N+1)
# for i in range(1, N+1):
#     D[i] = i
#     j = 1
#     while j*j <= i:
#         D[i] = min(D[i], D[i - j*j] + 1)
#         j += 1 
        
# print(D[N])


# 시간초과: http://blog.naver.com/occidere/220792326120
# N = int(input())

# D = [i for i in range(N+1)]
# for i in range(2, N+1):
#     j = 2
#     while j*j <= i:
#         D[i] = min(D[i], D[i - j*j] + 1)
#         j += 1 
# print(D[N])

# 틀렸습니다
# N = int(input())

# minim = 100000
# for i in range(2, int(N**0.5) + 1):
#     minim = min(minim, (N - i**2) + 1)

# print(minim)