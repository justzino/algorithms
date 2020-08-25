import sys

def checkPrime(num):
    is_prime = True
    i = 2
    if num < 2: 
        return False
        
    while i*i <= num:
        if num%i == 0:
            is_prime = False
            break
        i += 1
        
    return is_prime

num = int(input())
primes = list(map(int, input().split()))
result = 0

for i in primes:
    if checkPrime(i):
        result += 1

print(result)
