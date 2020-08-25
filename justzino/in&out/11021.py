n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print('Case #{}: {}'.format(i + 1, a + b))


# "출력형식"%(데이터....) : 이전 방식
# "출력형식".format(데이터...) : 파이썬(Python) 3 포맷팅 방식
