import sys

T = int(sys.stdin.readline())

D = [[0, 0, 0] for row in range(100001)] # 메모리초과, 런타임에러

D[1][0] = 1 # D[1] = [1, 0, 0] 이렇게 바꿔쓸 수 있음
D[2][1] = 1
D[3][0] = 1
D[3][1] = 1
D[3][2] = 1

for i in range(4, 100001): # 런타임에러
    D[i][0] = (D[i-1][1] + D[i-1][2])%1000000009
    D[i][1] = (D[i-2][0] + D[i-2][2])%1000000009
    D[i][2] = (D[i-3][0] + D[i-3][1])%1000000009

for i in range(T):
    idx = int(sys.stdin.readline())
    print((D[idx][0] + D[idx][1] + D[idx][2])%1000000009)

# 런타임에러: 배열크기
# 메모리초과: index 1,2,3 을 위해 4개를 쓴 것 -> 3개만...