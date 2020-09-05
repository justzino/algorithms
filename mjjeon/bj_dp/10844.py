N = int(input())
D = [[0,0,0,0,0,0,0,0,0,0] for i in range(101)]
D[1] = [0,1,1,1,1,1,1,1,1,1]

for i in range(2, N+1):
    D[i][0] = D[i-1][1]
    for j in range(1, 9):
        D[i][j] = D[i-1][j-1] + D[i-1][j+1]
    D[i][9] = D[i-1][8]

print(sum(D[N])%1000000000)



# 참고, 조금 변형함.: https://mygumi.tistory.com/260, https://sihyungyou.github.io/baekjoon-10844/

# 틀렸습니다
# N = int(input())
# D = [0] * 101
# D[1] = 9
# D[2] = D[1]*2-1

# for i in range(3, N):
#     D[i] = D[i-1]*2 - 1 

# print(D[N]%1000000000)