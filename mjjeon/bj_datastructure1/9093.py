import sys

cnt = int(sys.stdin.readline().rstrip())

temp_list = ['']*cnt
while_cnt = 0
while while_cnt < cnt:
    temp_list[while_cnt] = sys.stdin.readline().rstrip()
    while_cnt += 1

while_cnt = 0
while while_cnt < cnt:
    last_print_idx = 0
    current_len = len(temp_list[while_cnt])
    for i in range(current_len):
        if temp_list[while_cnt][i] == " ":
            current_idx = i - 1
            while last_print_idx <= current_idx:
                print(temp_list[while_cnt][current_idx], end='')
                current_idx -= 1
            print(" ", end='')
            last_print_idx = i + 1
        if i == current_len - 1:
            current_idx = i
            while last_print_idx <= current_idx:
                print(temp_list[while_cnt][current_idx], end='')
                current_idx -= 1

    while_cnt += 1
    print()