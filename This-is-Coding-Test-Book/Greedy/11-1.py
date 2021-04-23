n = int(input())
data = list(map(int, input().split()))

count = 0
data.sort()
group = []

for fear in data:
    group.append(fear)
    if len(group) == fear:
        count += 1
        group = []

print(count)
