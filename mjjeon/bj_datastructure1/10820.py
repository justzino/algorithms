import sys

while True:
    try:
        # lower, upper, number, space
        result = [0, 0, 0, 0]
        for i in input():
            if i.islower():
                result[0] += 1
            elif i.isupper():
                result[1] += 1
            elif i.isdigit():
                result[2] += 1
            elif i == " ":
                result[3] += 1
        print(*result)
    except EOFError:
        break