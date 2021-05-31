prime = [2, 3]

for n in range(5, 1001, 2):
    flag = 0
    for p in prime:
        if p * p > n:
            break
        if n % p == 0:
            flag = 1
            break
    if flag == 0:
        prime.append(n)

print(*prime)
