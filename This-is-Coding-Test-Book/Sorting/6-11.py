n = int(input())

data = []
for _ in range(n):
    a, b = input().split()
    data.append([int(b), a])

data.sort()

for i in range(n):
    print(data[i][1], end=' ')
