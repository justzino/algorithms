s = input()

result = []
for i in range(len(s)):
    result.append(s[i:])

print('\n'.join(map(str, sorted(result))))
