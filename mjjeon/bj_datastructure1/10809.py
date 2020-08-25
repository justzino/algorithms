alpha = [-1]*26
idx = 0
for i in input():
    if alpha[ord(i) - 97] == -1:
        alpha[ord(i) - 97] = idx
    idx += 1

print(*alpha)