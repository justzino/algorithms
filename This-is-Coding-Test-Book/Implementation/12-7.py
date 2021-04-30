n = input()
mid = len(n) // 2

l, r = n[:mid], n[mid:]
left, right = 0, 0

for i in l:
    left += int(i)
for i in r:
    right += int(i)

if left == right:
    print("LUCKY")
else:
    print("READY")
