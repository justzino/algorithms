# a진법 -> b진법
def notation(num, n, a, b):
    tmp, result = 0, []
    # a->10
    for i in range(num):
        tmp += (n.pop() * (a ** i))

    while tmp >= b:
        remainder = tmp % b
        tmp = tmp // b
        result.append(remainder)
    if tmp > 0:
        result.append(tmp)

    return reversed(result)


A, B = map(int, input().split())
m = int(input())
nums = list(map(int, input().split()))

print(*notation(m, nums, A, B))
