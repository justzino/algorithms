N = int(input())

last = 2

while N != 1:
    div = N%last
    if div != 0:
        last += 1
    else:
        print(last)
        N = N//last
