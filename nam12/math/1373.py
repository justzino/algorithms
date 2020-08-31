# x = input()

# sum = 0
# location = 0


# for i in x[::-1]:
#     if i == '1':
#         sum += 2**location
#     location += 1

# print(format(sum, 'o'))

# 2 -> 10 -> 8 진수로 바꾸니 시간초과뜸.


# x = int(input(), 2)
# print(format(x, 'o'))


print(oct(int(input(), 2))[2:])
