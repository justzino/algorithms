N = int(input())
D = [[0,0,0,0,0,0,0,0,0,0] for i in range(N+1)]
D[1] = [1,1,1,1,1,1,1,1,1,1]
for i in range(2, N+1):
    for j in range(10):
        idx = j
        while idx <= 9:
            D[i][j] += D[i-1][idx]
            idx += 1
    
print(sum(D[N])%10007)