s = input().rstrip()
result = 0

for i in s:
    n = int(i)
    if n <= 1 or result <= 1:
        result += n
    else:
        result *= n

print(result)
