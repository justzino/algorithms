N = int(input())


# i = 2
# while N:

#     if N == i:
#         print(i)
#         break

#     if N % i == 0:
#         print(i)
#         N //= i
#         i = 2
#         continue
#     i += 1

for i in range(2, N+1):

    if N < 2:
        break

    while N % i == 0:
        print(i)
        N //= i
