import sys

T = int(sys.stdin.readline())

for i in range(T):

    n = int(sys.stdin.readline())
    # 1309 처럼 되도록 이어붙임
    sticker_list = [0] * n*2
    sticker1 = list(map(int, sys.stdin.readline().split()))
    sticker2 = list(map(int, sys.stdin.readline().split()))
    for i in range(0, n):
        sticker_list[i*2] = sticker2[i]
        sticker_list[(i*2)+1] = sticker1[i]
    # 1309 처럼인데 가중치로 값 계산
    D = [[0, 0, 0] for i in range(n+1)]
    D[1] = [0, sticker_list[0], sticker_list[1]] # 없는 경우, 왼쪽, 오른쪽
    for i in range(2, n+1):
        D[i][0] = max(D[i-1][0], D[i-1][1], D[i-1][2])
        D[i][1] = max(D[i-1][0], D[i-1][2]) + sticker_list[(i-1)*2]
        D[i][2] = max(D[i-1][0], D[i-1][1]) + sticker_list[(i-1)*2+1]

    print(max(D[n]))
