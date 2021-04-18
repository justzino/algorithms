# 집합 자료형
n = int(input())
# 가게에 있는 전체 부품 번호를 입력받아서 집합(set) 자료형에 기록
parts = set(map(int, input().split()))

m = int(input())
orders = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for order in orders:
    if order in parts:
        print('yes', end=' ')
    else:
        print('no', end=' ')
