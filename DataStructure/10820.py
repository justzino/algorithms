import sys

for line in sys.stdin:
    result = [0, 0, 0, 0]

    for c in line:
        if 'a' <= c <= 'z':     # c.islower()
            result[0] += 1
        elif 'A' <= c <= 'Z':   # c.isupper()
            result[1] += 1
        elif '0' <= c <= '9':   # c.isdigit()
            result[2] += 1
        elif c == ' ':
            result[3] += 1
    print(' '.join(map(str, result)))
