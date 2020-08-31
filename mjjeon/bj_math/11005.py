import sys
N, B = map(int, sys.stdin.readline().rstrip().split())

# B 진법...
result = ''
quot = N
if quot == 0:
    result = '0'
while quot != 0:
    div = quot%(B)
    quot = quot//(B)
    if div != 0:
        if div > 9:
            result = chr(div + 55) + result
        else:
            result = str(div) + result
    else:
        result = '0' + result # 여기 부분...!
    # 여기 if, else 좀 더 줄일 수 있음..
    # divmod 라는 함수를 사용해서 몫과 나머지 한번에,
    # if 나머지 > 9 라고만 줘도 구현 가능.
print(result)
