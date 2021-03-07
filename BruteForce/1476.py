E, S, M = map(int, input().rstrip().split())

max_e, max_s, max_m = 15, 28, 19
e, s, m = 1, 1, 1
year = 1

while e != E or s != S or m != M:
    e += 1
    s += 1
    m += 1
    year += 1

    if e > max_e:
        e = 1
    if s > max_s:
        s = 1
    if m > max_m:
        m = 1

print(year)
