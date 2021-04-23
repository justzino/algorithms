n = int(input())
data = list(map(int, input().split()))

result = 0
count = 0
data.sort()

for fear in data:
    count += 1
    if count >= fear:
        result += 1
        count = 0

print(count)
