number = input()
if '-' in number:
    print(str(oct(int('0b' + number, 2)))[2:])
else:
