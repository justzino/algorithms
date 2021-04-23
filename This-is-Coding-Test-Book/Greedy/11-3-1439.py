s = input()

count = 1
last = s[0]

for i in s[1:]:
    if last != i:
        count += 1
    last = i

print(count // 2)
