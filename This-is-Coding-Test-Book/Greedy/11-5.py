n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11

for i in data:
    array[i] += 1

result = 0

for i in range(1, m + 1):
    for j in range(i + 1, n):
        if data[i] == data[j]:
            continue
        result += 1

print(result)
