# n진법 -> 10진법(int)
def notation(num, n):
    n_set = {chr(ord('A')+i-10): i for i in range(10, n)}      # {'A': 10, 'B': 11, 'C': 12, 'D': 13, ...}
    result = 0
    l = len(num)

    for i in range(l):
        if num[-1].isupper():
            result += n_set[num.pop()] * (n ** i)
        elif num[-1].isdigit():
            result += int(num.pop()) * (n ** i)

    return result


N, B = input().split()

print(notation(list(N), int(B)))
