import sys

string = list(sys.stdin.readline())
A, Z, a, z = ord('A'), ord('Z'), ord('a'), ord('z')

for c in string:
    s = ord(c)
    if A <= s <= Z:
        if s + 13 > Z:
            print(chr(A + s + 12 - Z), end='')
        else:
            print(chr(s + 13), end='')
    elif a <= s <= z:
        if s + 13 > z:
            print(chr(a + s + 12 - z), end='')
        else:
            print(chr(s + 13), end='')
    else:
        print(c, end='')
