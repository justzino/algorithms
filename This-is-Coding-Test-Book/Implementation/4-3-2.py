# 방법 2. steps 로 이동할 수 있는 방향을 기록
data = input()

# x, y축 input 을 index 로 변경시키는 작업
x = int(data[1])
y = int(ord(data[0])) - int(ord('a')) + 1

# 움직일 수 있는 방향
steps = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

count = 0

for step in steps:
    nx = x + step[0]
    ny = y + step[1]

    # 좌표 벗어나면 무시
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    else:
        count += 1

print(count)
