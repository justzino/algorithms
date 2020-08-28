6588 번 :

================
9613 번 :

<!-- from itertools import combinations
from sys import stdin
input = stdin.readline

def gcd(a,b):
    if b == 0: # 나머지
        return a # 최대공약수
    return gcd(b,a%b)

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    ans = 0
    for e in list(combinations(arr[1:], 2)):
        if e[0] > e[1]:
            ans += gcd(e[0], e[1])
        else:
            ans += gcd(e[1], e[0])
    print(ans)

에서 처럼 from itertools로 combinations 사용 가능

for e in list(combinations(arr[1:],2)):
    if e[0] > e[1]: #nCm 에서 n > m 을 나타낸 것이다. -->

https://python.flowdas.com/library/itertools.html 에서 iterator들 확인해보기!
