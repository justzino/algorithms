n = int(input())
data = list(map(str, input().split()))

start = [1, 1]

for direction in data:
    if direction == 'U':
        if start[0] == 1:
            continue
        else:
            start[0] += -1

    elif direction == 'D':
        if start[0] == 5:
            continue
        else:
            start[0] += 1

    elif direction == 'L':
        if start[1] == 1:
            continue
        else:
            start[1] += -1

    elif direction == 'R':
        if start[1] == 5:
            continue
        else:
            start[1] += 1

print(start[0], start[1])
