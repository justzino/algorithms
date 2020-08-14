n_line = int(input())

if 1 <= n_line and n_line <= 100:
    for i in range(1, n_line+1):
        print(" "*(n_line-i), end='')
        print("* "*i)