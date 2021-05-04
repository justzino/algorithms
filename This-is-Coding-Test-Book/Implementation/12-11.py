from collections import deque

n = int(input())
matrix = [[-1] * (n+1)] + [[-1] + [0] * n for _ in range(n+1)]

k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    matrix[x][y] = 1

m = int(input())
op = deque([])

for _ in range(m):
    t, s = input().split()
    op.append((int(t), s))

rotate = {'D': 1, 'L': -1}
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

x, y = 1, 1
head_direction = 0

time = 0
q = deque([])       # 뱀 위치

# (1, 1) 에서 시작
q.append((x, y))
matrix[x][y] = -1

while True:
    x += direction[head_direction][0]
    y += direction[head_direction][1]

    # 벽 or 자기자신과 부딪힌 경우 return time
    if x > n or y > n or matrix[x][y] == -1:
        break

    elif matrix[x][y] == 0:
        a, b = q.popleft()
        matrix[a][b] = 0
        q.append((x, y))
        matrix[x][y] = -1

    elif matrix[x][y] == 1:
        q.append((x, y))
        matrix[x][y] = -1

    time += 1
    if op and op[0][0] == time:
        t, d = op.popleft()
        head_direction = (head_direction + rotate[d]) % 4

print(time + 1)
