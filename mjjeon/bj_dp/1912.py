n = int(input())
N = list(map(int, input().split()))

result = 0

# 이전까지 것을 더한 것을 저장해놔야될것 같은데? 굿~
D = [0] * n

for i in range(n):
    D[i] = max(N[i], D[i-1] + N[i])
    
print(max(D))