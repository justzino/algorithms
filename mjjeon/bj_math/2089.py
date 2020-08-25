number = int(input()) 
result = ''
quot = number
if number == 0:
    result = '0'
while quot != 0:
    div = quot%(-2)
    quot = quot//(-2)
    if div == -1:
        quot += 1
        result = '1' + result
    else:
        result = '0' + result
print(result)

# 0일 경우도 확인해줘야함..

# 틀렸습니다..
# number = int(input())
# result = ''
# quot = number
# while quot != 0:
#     div = quot%(-2)
#     quot = quot//(-2)
#     if div == -1:
#         quot += 1
#         result = '1' + result
#     else:
#         result = '0' + result
# print(result)


# 틀렸습니다..
# 나머지를 아래에서부터 올라와야함..
# number = int(input())
# result = ''
# quot = number
# if number < 0:
#     while quot != 0:
#         div = quot%(-2)
#         quot = quot//(-2)
#         if div == -1:
#             quot += 1
#             result += '1'
#         else:
#             result += '0'
#     print(result)
# else:
#     print(bin(int(number))[2:])