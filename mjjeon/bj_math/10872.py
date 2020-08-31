n = int(input())
result = 1
if n > 1:
    for i in range(2, n+1):
        result = result * i
print(result)
