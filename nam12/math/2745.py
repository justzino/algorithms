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

import sys

N, B = sys.stdin.readline().rstrip().split()
B = int(B)

ans, i = 0, 0

for char in N[::-1]:

    if char.isupper():
        ans += (ord(char) - 55) * (B**i)
    else:
        ans += int(char)
    i += 1
print(ans)
