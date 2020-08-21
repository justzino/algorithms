# 테스트 케이스의 갯수가 주어지지 않는 문제

# sol 1
# python 예외 처리에 대하여
# https://wikidocs.net/30#_1
try:
    while 1:
        a, b = map(int, input().split())
        print(a + b)

except:
    exit()

# sol 2
# input /
# sys.stdin과 sys.stdin.readline()
import sys

for line in sys.stdin:
    a, b = map(int, line.split())
    print(a+b)
