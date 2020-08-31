import sys

def TentoB(B, number):
    result = []
    quot = number
    if quot == 0:
        result.append(0)
    while quot != 0:
        div = quot%(B)
        quot = quot//(B)
        result.append(div)  # 여기 알파벳이 아니고 숫자 그대로 뽑아줘야.. 
        
    return result[::-1]

A, B = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline().rstrip())
numbers = list(sys.stdin.readline().split())

result = 0
b = 0
for i in numbers[::-1]:
    result += int(i) * (A ** b)
    b += 1

print(*TentoB(B, result))



# def AtoTen(A, number):
#     result = 0
#     b = 0
#     for i in str(number)[::-1]:
#         if i.isupper():
#             result += (ord(i) - 55) * (A**b)
#         else:
#             result += int(i)*(A**b)
#         b += 1
#     return result
