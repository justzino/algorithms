def check(x, y, n):
    num = array[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if array[i][j] != num:
                return False
    if num == -1:
        answer[0] += 1
    elif num == 0:
        answer[1] += 1
    else:
        answer[2] += 1
    return True


def divide(x, y, n):
    if check(x, y, n):
        return

    k = n // 3
    for i in range(3):
        for j in range(3):
            divide(x + i*k, y + j*k, k)


N = int(input())
array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

answer = [0, 0, 0]
divide(0, 0, N)
for i in range(3):
    print(answer[i])