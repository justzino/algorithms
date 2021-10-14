def func(r, c, n):
    if n == 0:
        return 0

    HALF = 1 << (n-1)
    if r < HALF and c < HALF:
        return func(r, c, n-1)
    elif r < HALF and c >= HALF:
        return HALF*HALF + func(r, c-HALF, n-1)
    elif r >= HALF and c < HALF:
        return HALF*HALF*2 + func(r-HALF, c, n-1)
    else:
        return HALF*HALF*3 + func(r-HALF, c-HALF, n-1)


N, r, c = map(int, input().split())


print(func(r, c, N))