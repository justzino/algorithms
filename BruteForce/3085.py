from sys import stdin

N = int(stdin.readline())
candies = [list(stdin.readline().rstrip()) for _ in range(N)]
max_candies = 0


def check(board, m, n):
    cnt1 = 1
    cnt2 = 1
    # 가로줄 왼쪽
    for x in range(n):
        if board[m][n - x] == board[m][n - x - 1]:
            cnt1 += 1
            continue
        break
    # 가로줄 오른쪽
    for x in range(n, N-1):
        if board[m][x] == board[m][x + 1]:
            cnt1 += 1
            continue
        break

    # 세로줄 위
    for y in range(m):
        if board[m - y][n] == board[m - y - 1][n]:
            cnt2 += 1
            continue
        break
    # 세로줄 아래
    for y in range(m, N-1):
        if board[y][n] == board[y + 1][n]:
            cnt2 += 1
            continue
        break

    return max(cnt1, cnt2)


for i in range(N):
    # 가로 바꾸기
    for j in range(N - 1):
        max_candies = max(max_candies, check(candies, i, j))
        candies[i][j], candies[i][j + 1] = candies[i][j + 1], candies[i][j]
        max_candies = max(max_candies, check(candies, i, j))
        candies[i][j], candies[i][j + 1] = candies[i][j + 1], candies[i][j]
    # 세로 바꾸기
for i in range(N-1):
    for j in range(N):
        candies[i][j], candies[i + 1][j] = candies[i + 1][j], candies[i][j]
        max_candies = max(max_candies, check(candies, i, j))

print(max_candies)