# 방법 1. dx, dy 리스트를 활용하여 이동할 방향 기록
data = input()

# x, y축 input 을 index 로 변경시키는 작업
x = int(data[1])
y_types = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
y = y_types.index(data[0]) + 1

# 움직일 수 있는 방향
dx = [1, 1, -1, -1, 2, 2, -2, -2]
dy = [2, -2, 2, -2, 1, -1, 1, -1]

count = 0

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]

    # 좌표 벗어나면 무시
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    else:
        count += 1

print(count)
