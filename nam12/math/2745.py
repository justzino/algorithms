# import sys

# N, B = sys.stdin.readline().rstrip().split()

# B = int(B)
# ans = 0


# for i in range(len(N)-1, -1, -1):
#     if N[i].isupper():
#         ans += (ord(N[i])-55)*(B**i)
#     else:
#         ans += int(N[i])
# print(str(ans))


# N, B = sys.stdin.readline().rstrip().split()
# B = int(B)

# ans, i = 0, 0

# for char in N[::-1]:

#     if char.isupper():
#         ans += (ord(char) - 55) * (B**i)
#     else:
#         ans += int(char)
#     i += 1
# print(ans)


# dict2 = {
#     '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
#     'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18,
#     'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27,
#     'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35
# }

# N, B = input().split()
# B = int(B)

# ans = 0
# for i, b in enumerate(N[::-1]):
#     ans = ans + dict2[b] * (B**i)
#     print("i, b :", i, b)

# print(ans)
# enumerate를 써서 index와 key값이 동시에 나오게 가능.
# 그리고 key = > value를 얻을 수 있다.


# before, base = sys.stdin.readline().split()
# base = int(base)
# cnt, res = 0, 0
# for c in before[::-1]:
#     target = int(c) if c.isdigit() else ord(c) - 55
#     res += (target * (base**cnt))
#     cnt += 1
# sys.stdout.write(str(res))
# testing code
