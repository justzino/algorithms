n_line = int(input())

if 1 <= n_line and n_line <= 100:
    for i in range(1, n_line+1):
        print(" "*(n_line-i), end='')
        if i == 1 or i == n_line:
            print("*"*(i*2-1))
        else:
            print("*", end='')
            print(" "*((i-1)*2-1), end='')
            print("*")