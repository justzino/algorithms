str_line = input()
for i in range(0, len(str_line)):
    if i % 10 == 0 and i != 0:
        print()
    print(str_line[i], end='')