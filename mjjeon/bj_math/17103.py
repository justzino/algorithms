import sys
cnt = int(sys.stdin.readline().rstrip())

# 에라토스테네스의 체로 소수 구하기. 1000000 이하..
seive = [False, False] + [True] * (1000000 - 1)
for (i, e) in enumerate(seive):
    if e:
        k = i * 2
        while k <= 1000000:
            seive[k] = False
            k += i
primes = []
for i, e in enumerate(seive):
    if e:
        primes.append(i)
primes_bool = [False] * (1000000 + 1) 
for i in primes:
    primes_bool[i] = True

for i in range(cnt):
    result = 0
    value = int(sys.stdin.readline())
    for i in range(int(value/2)+1): 
        if primes[i] <= value - primes[i]: # 런타임 에러 수정
            if primes_bool[value - primes[i]] == True:
                result += 1
        else:
            break
    print(result)


# for i in range(cnt):
#     result = 0
#     value = int(sys.stdin.readline())
#     for i in range(int(value/2) + 1): # for 문에서 런타임 에러나는 듯
#         if primes_bool[value - primes[i]] == True:
#             result += 1
#     result = result if result <= 1 else int(round(result/2))
#     print(result)