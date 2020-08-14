import sys

left_stack = list(sys.stdin.readline().rstrip())

if 1 <= len(left_stack) <= 100000:

    right_stack = []*len(left_stack)

    input_cnt = int(sys.stdin.readline().rstrip())

    if 1 <= input_cnt <= 500000:
        while_cnt = 0

        while while_cnt < input_cnt:

            input_command = sys.stdin.readline().rstrip().split()
        
            if input_command[0] == 'L':
                if len(left_stack) > 0:
                    right_stack.append(left_stack.pop())
            elif input_command[0] == 'D':
                if len(right_stack) > 0:
                    left_stack.append(right_stack.pop())
            elif input_command[0] == 'B':
                if len(left_stack) > 0:
                    left_stack.pop()
            elif input_command[0] == 'P':
                left_stack.append(input_command[1])
            while_cnt += 1

        print(''.join(left_stack + right_stack[::-1]))

# https://suri78.tistory.com/112

# list index 사용으로 시간초과

# import sys

# input_line = sys.stdin.readline().rstrip()

# if 1 <= len(input_line) <= 100000:

#     input_cnt = int(sys.stdin.readline().rstrip())

#     if 1 <= input_cnt <= 500000:
#         while_cnt = 0

#         cursor_idx = len(input_line)
        
#         while while_cnt < input_cnt:

#             input_command = sys.stdin.readline().rstrip().split()
        
#             if input_command[0] == 'L':
#                 if cursor_idx > 0: cursor_idx -= 1
#             elif input_command[0] == 'D':
#                 if cursor_idx < len(input_line): cursor_idx += 1
#             elif input_command[0] == 'B':
#                 if cursor_idx == len(input_line):
#                     input_line = input_line[:cursor_idx-1]
#                     cursor_idx -= 1
#                 elif cursor_idx > 0:
#                     input_line = input_line[:cursor_idx-1] + input_line[cursor_idx:]
#                     cursor_idx -= 1
#             elif input_command[0] == 'P':
#                 if cursor_idx == 0:
#                     input_line = input_command[1] + input_line
#                 elif cursor_idx < len(input_line):
#                     input_line = input_line[:cursor_idx] + input_command[1] + input_line[cursor_idx:]
#                 else:
#                     input_line = input_line + input_command[1]
#                 cursor_idx += 1
#             while_cnt += 1

#         print(input_line)