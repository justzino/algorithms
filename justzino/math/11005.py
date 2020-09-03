# 10진법 -> n진법(문자열)
def notation(num, n):
    n_set = {i: chr(ord('A')+i-10) for i in range(10, n+1)}      # {10: 'A', 11: 'B', 12: 'C', 13, ...}
    result = ''

    while num >= n:
        remainder = num % n
        num = num // n
        if remainder > 9:
            result += n_set[remainder]
        else:       # remainder <= 9
            result += str(remainder)
    if num > 9:
        result += n_set[num]
    elif num > 0:
        result += str(num)

    return result[::-1]


N, B = map(int, input().split())

print(notation(N, B))
