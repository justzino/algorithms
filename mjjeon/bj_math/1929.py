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

a, b = map(int, input().split())
result = []

for i in range(a, b+1):
    if checkPrime(i):
        print(i)

