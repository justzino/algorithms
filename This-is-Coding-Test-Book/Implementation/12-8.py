string = input()

num = []
result = []
for s in string:
    if s.isdigit():
        num.append(int(s))
    else:
        result.append(s)

result.sort()
s = sum(num)
result += str(s)
print(''.join(result))

# K1KA5CB7
# AJKDLSI412K4JSJ9D
