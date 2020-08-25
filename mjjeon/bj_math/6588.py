import sys

number = -1
# 소수 찾기
seive = [False, False] + [True] * (1000000 - 1)
for i, e in enumerate(seive):
    if e:
        k = i * 2
        while k <= 1000000:
            seive[k] = False
            k += i
primes = [x for (x, y) in enumerate(seive) if y]
primes = primes[1:] # 2 제외 
primes_bool = [False]*1000001 # index로 바로 찾게 하기 위해
for i in primes:
    primes_bool[i] = True

while number != 0:
    is_find = False
    number = int(sys.stdin.readline().rstrip())

    for i in range(int(number/2)):
        if primes_bool[number - primes[i]] == True:
            print('{0} = {1} + {2}'.format(number, primes[i], number - primes[i]))
            is_find = True
            break 

    if not is_find and number != 0:
        print("Goldbach's conjecture is wrong.")
        break



# https://somjang.tistory.com/entry/BaeKJoon-6588%EB%B2%88-%EA%B3%A8%EB%93%9C%EB%B0%94%ED%9D%90%EC%9D%98-%EC%B6%94%EC%B8%A1-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4

# 시간초과

# import sys

# def checkPrime(num):
#     is_prime = True
#     i = 2
#     while i*i <= num:
#         if num%i == 0:
#             is_prime = False
#             break
#         i += 1
        
#     return is_prime

# number = -1
# primes = []

# # 소수 찾기
# for i in range(3, 1000000, 2):
#     if checkPrime(i):
#         primes.append(i)

# while number != 0:
#     is_find = False
#     number = int(sys.stdin.readline().rstrip())

#     # 더하기 확인
#     # 입력받은 값보다 작은 소수 인덱스 구하기
#     idx = 0
#     while primes[idx] < number:
#         idx += 1

#     start_idx = idx - 1 if idx > 0 else idx
#     end_idx = 0
#     while start_idx > end_idx and start_idx <= len(primes) - 1 and end_idx >= 0:
#         if primes[start_idx] + primes[end_idx] > number:
#             start_idx -= 1
#         elif primes[start_idx] + primes[end_idx] < number:
#             end_idx += 1
#         elif primes[start_idx] + primes[end_idx == number]:
#             is_find = True
#             break
    
#     if is_find:
#         print('{0} = {1} + {2}'.format(number, primes[end_idx], primes[start_idx]))
#     else:
#         print("Goldbach's conjecture is wrong.")
    