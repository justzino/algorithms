# 계수 정렬 사용
n = int(input())

parts = [False] * 1000001
array = list(map(int, input().split()))
for i in array:
    parts[i] = True

m = int(input())
orders = list(map(int, input().split()))

for order in orders:
    if parts[order]:
        print('yes', end=' ')
    else:
        print('no', end=' ')
