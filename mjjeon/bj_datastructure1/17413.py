import sys
input_val = sys.stdin.readline().rstrip()
cnt = len(input_val)
i = 0
is_open = False
last_idx = 0
while i < cnt: 
    if input_val[i] == "<":
        is_open = True
        if last_idx < i and i != 0:
            curr_idx = i - 1
            while last_idx <= curr_idx:
                print(input_val[curr_idx], end='')
                curr_idx -= 1
    elif input_val[i] == ">":
        is_open = False
        print(input_val[i], end='')
        last_idx = i + 1

    if not is_open and input_val[i] == " ":
        curr_idx = i - 1
        while last_idx <= curr_idx:
            print(input_val[curr_idx], end='')
            curr_idx -= 1
        print(input_val[i], end='')    
        last_idx = i + 1
    elif is_open:
        print(input_val[i], end='')
    else:
        pass

    if i == cnt - 1 and not is_open:
        curr_idx = i
        while last_idx <= curr_idx:
            print(input_val[curr_idx], end='')
            curr_idx -= 1

    i += 1