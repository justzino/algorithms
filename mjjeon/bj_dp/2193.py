N = int(input())
D = [0]*91
D[0] = 0
D[1] = 1
D[2] = 1
D[3] = 2
for i in range(4, N+1):
    D[i] = D[i-1] + D[i-2]

print(D[N])

# 처음으로 진짜 나혼자 힘으로 풀었다...