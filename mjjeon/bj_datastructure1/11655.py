for i in input():
    if not i.isupper() and not i.islower():
        print(i, end='')
    else:
        value = ord(i) + 13
        if value > 122 and i.islower():
            print(str(chr(value - 123 + 97)), end='')
        elif value > 90 and i.isupper():
            print(str(chr(value - 91 + 65)), end='')
        else:
            print(chr(value), end='')