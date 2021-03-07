
string = input()

result = [0] * 26

for c in string:
    result[ord(c) - ord('a')] += 1

print(' '.join(map(str, result)))
# print(*result)
