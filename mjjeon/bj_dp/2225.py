N, K = map(int, input().split())

# D[K][N]
D = [[0 for i in range(201)] for i in range(201)]

# 1개의 숫자로만 더하면 1개
for i in range(201):
    D[1][i] = 1


# 2~K개를 더해서 0~N이 나오는 경우
# 이차원 배열이라 이중포문인데 
# 경우의 수를 다 더해야 하므로 포문이 한 개 더
for k in range(2, K+1):
    for n in range(N+1):
        for l in range(n+1):
            D[k][n] += D[k-1][l]

print(D[K][N]%1000000000)

# 참고
# https://yabmoons.tistory.com/128
# https://lmcoa15.tistory.com/64
# https://mygumi.tistory.com/135
# https://sihyungyou.github.io/baekjoon-2225/