import sys

cnt = int(sys.stdin.readline().rstrip())
result = [-1 for _ in range(cnt)]
stack = [] # index 를 저장해놓음..
if 1 <= cnt <= 1000000:
    input_list = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(cnt):

        while len(stack) != 0 and input_list[stack[-1]] < input_list[i]:
            result[stack.pop()] = input_list[i]
        
        stack.append(i)

    print(*result)

    


# import sys

# cnt = int(sys.stdin.readline().rstrip())
# result = ''
# if 1 <= cnt <= 1000000:
#     input_list = list(map(int, sys.stdin.readline().rstrip().split()))
#     while_idx = 0
#     while while_idx < cnt:
#         is_found = False
#         if while_idx == cnt - 1:
#             result += '-1'
#             # print('-1')
#         else:
#             in_while_idx = while_idx + 1
#             while in_while_idx < cnt:
#                 if input_list[while_idx] < input_list[in_while_idx]:
#                     is_found = True
#                     break
#                 in_while_idx += 1

#             if is_found:
#                 result += str(input_list[in_while_idx]) + ' '
#                 # print(input_list[in_while_idx], end=' ')
#             else:
#                 result += '-1 '
#         while_idx += 1

# print(result)