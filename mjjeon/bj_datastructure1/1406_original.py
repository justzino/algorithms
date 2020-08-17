# unsolved...
# 입력을 계속 받음,,,

import sys

input_line = sys.stdin.readline().rstrip()

input_cnt = int(sys.stdin.readline().rstrip())
input_line_cnt = len(input_line)

cursor_idx = len(input_line)

for input_command in sys.stdin:

    if input_command[0] == 'L':
        if cursor_idx > 0: cursor_idx -= 1
    elif input_command[0] == 'D':
        if cursor_idx < input_line_cnt: cursor_idx += 1
    elif input_command[0] == 'B':
        if cursor_idx == input_line_cnt:
            input_line = input_line[:cursor_idx-1]
            cursor_idx -= 1
            input_line_cnt -= 1
        elif cursor_idx > 0:
            input_line = input_line[:cursor_idx-1] + input_line[cursor_idx:]
            cursor_idx -= 1
            input_line_cnt -= 1
    elif input_command[0] == 'P':
        if cursor_idx == 0:
            # input_line = input_command[1] + input_line
            input_line = input_command[2] + input_line
        elif cursor_idx < input_line_cnt:
            # input_line = input_line[:cursor_idx] + input_command[1] + input_line[cursor_idx:]
            input_line = input_line[:cursor_idx] + input_command[2] + input_line[cursor_idx:]
        else:
            # input_line = input_line + input_command[1]
            input_line = input_line + input_command[2]
        input_line_cnt += 1
        cursor_idx += 1

print(input_line)