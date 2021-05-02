n = int(input())
data = list(map(int, input().split()))

stack = []
result = [-1] * n

for i in range(n):
    try:
        while data[stack[-1]] < data[i]:
            num = stack.pop()
            result[num] = data[i]
    except IndexError:
        pass
    stack.append(i)

print(*result)
